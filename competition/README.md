# Competition Scoring (Instructor)

This folder contains instructor tooling for ranking challenge submissions.

## Ranking policy
- Primary metric: **PR-AUC** (`average_precision_score`)
- Tie-breaker 1: **F1** at threshold `0.50`
- Tie-breaker 2: lower **log loss**

## Input formats
- Private labels CSV: `id,y_true`
- Student submission CSV: `id,y_prob`

## Run scorer
```bash
python competition/competition_score_bank_marketing.py \
  --labels private_labels.csv \
  --submissions submissions \
  --out leaderboard.csv
```

## Typical workflow
1. Collect all student submission CSV files in one folder.
2. Keep private labels local (do not commit to public repo).
3. Run scorer and use `leaderboard.csv` to select top 3 winners.

