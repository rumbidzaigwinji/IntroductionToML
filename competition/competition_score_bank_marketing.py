from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, f1_score, log_loss


def _normalize_binary_label(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        vals = series.dropna().unique()
        if set(vals).issubset({0, 1}):
            return series.astype(int)
        raise ValueError("Numeric label column must contain only 0/1 values.")

    mapped = (
        series.astype(str)
        .str.strip()
        .str.lower()
        .map({"0": 0, "1": 1, "no": 0, "yes": 1, "false": 0, "true": 1})
    )
    if mapped.isna().any():
        bad = series[mapped.isna()].head(5).tolist()
        raise ValueError(f"Could not map some label values to binary classes: {bad}")
    return mapped.astype(int)


def _validate_submission_frame(df: pd.DataFrame, submission_path: Path) -> pd.DataFrame:
    required = {"id", "y_prob"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"{submission_path.name}: missing required columns: {sorted(missing)}")

    if df["id"].duplicated().any():
        raise ValueError(f"{submission_path.name}: duplicate ids detected.")

    df = df.copy()
    df["y_prob"] = pd.to_numeric(df["y_prob"], errors="coerce")
    if df["y_prob"].isna().any():
        raise ValueError(f"{submission_path.name}: y_prob contains non-numeric values.")

    if ((df["y_prob"] < 0) | (df["y_prob"] > 1)).any():
        raise ValueError(f"{submission_path.name}: y_prob must be within [0, 1].")

    return df


def _score_submission(
    truth: pd.DataFrame,
    submission_path: Path,
    threshold: float,
) -> dict[str, float | str]:
    pred = pd.read_csv(submission_path)
    pred = _validate_submission_frame(pred, submission_path)

    merged = truth.merge(pred, on="id", how="left", validate="one_to_one")
    if merged["y_prob"].isna().any():
        missing = int(merged["y_prob"].isna().sum())
        raise ValueError(f"{submission_path.name}: missing predictions for {missing} ids.")

    y_true = merged["y_true"].to_numpy()
    y_prob = merged["y_prob"].to_numpy()
    y_hat = (y_prob >= threshold).astype(int)

    return {
        "submission": submission_path.name,
        "pr_auc": float(average_precision_score(y_true, y_prob)),
        "f1_at_threshold": float(f1_score(y_true, y_hat)),
        "log_loss": float(log_loss(y_true, y_prob, labels=[0, 1])),
    }


def score_all_submissions(
    labels_csv: Path,
    submissions_dir: Path,
    threshold: float,
) -> pd.DataFrame:
    truth = pd.read_csv(labels_csv)
    required = {"id", "y_true"}
    missing = required - set(truth.columns)
    if missing:
        raise ValueError(f"Labels file missing required columns: {sorted(missing)}")

    if truth["id"].duplicated().any():
        raise ValueError("Labels file has duplicate ids.")

    truth = truth.copy()
    truth["y_true"] = _normalize_binary_label(truth["y_true"])

    submission_files = sorted(submissions_dir.glob("*.csv"))
    if not submission_files:
        raise FileNotFoundError(f"No CSV submissions found in: {submissions_dir}")

    rows = []
    for path in submission_files:
        try:
            rows.append(_score_submission(truth, path, threshold))
        except Exception as exc:
            rows.append(
                {
                    "submission": path.name,
                    "pr_auc": np.nan,
                    "f1_at_threshold": np.nan,
                    "log_loss": np.nan,
                    "error": str(exc),
                }
            )

    result = pd.DataFrame(rows)
    if "error" not in result.columns:
        result["error"] = ""
    else:
        result["error"] = result["error"].fillna("")

    valid = result[result["error"] == ""].copy()
    invalid = result[result["error"] != ""].copy()

    if not valid.empty:
        valid = valid.sort_values(
            by=["pr_auc", "f1_at_threshold", "log_loss", "submission"],
            ascending=[False, False, True, True],
        ).reset_index(drop=True)
        valid.insert(0, "rank", valid.index + 1)
    else:
        valid.insert(0, "rank", [])

    if not invalid.empty:
        invalid = invalid.sort_values("submission").reset_index(drop=True)
        invalid.insert(0, "rank", np.nan)

    return pd.concat([valid, invalid], ignore_index=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Score Bank Marketing competition submissions and produce a ranked leaderboard.",
    )
    parser.add_argument(
        "--labels",
        type=Path,
        required=True,
        help="CSV with columns: id, y_true (0/1 or no/yes). Keep this private.",
    )
    parser.add_argument(
        "--submissions",
        type=Path,
        required=True,
        help="Folder containing student submission CSV files (columns: id, y_prob).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("leaderboard_bank_marketing.csv"),
        help="Output leaderboard CSV path.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.50,
        help="Probability threshold used for F1 tie-breaker (default: 0.50).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    leaderboard = score_all_submissions(args.labels, args.submissions, args.threshold)
    leaderboard.to_csv(args.out, index=False)

    print(f"Saved leaderboard: {args.out.resolve()}")
    if "error" in leaderboard.columns and (leaderboard["error"] != "").any():
        bad = leaderboard[leaderboard["error"] != ""]
        print(f"Invalid submissions: {len(bad)} (see 'error' column in the CSV)")

    cols = ["rank", "submission", "pr_auc", "f1_at_threshold", "log_loss"]
    existing_cols = [c for c in cols if c in leaderboard.columns]
    print("\nTop results:")
    print(leaderboard[existing_cols].head(10).to_string(index=False))


if __name__ == "__main__":
    main()

