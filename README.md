# IndabaX Zimbabwe - Intro to ML (Full Course Repo)

This repository contains the full course stack:
- slide deck,
- structured module notes,
- practical notebooks,
- challenge competition workflow.

## Start Here

### 1) Course overview
- Slides: [`slides/IndabaX_Zimbabwe_Intro_to_ML.pptx`](./slides/IndabaX_Zimbabwe_Intro_to_ML.pptx)
- Curriculum notes (mapped to slides): [`modules/README.md`](./modules/README.md)
- Notebook track: [`notebooks/README.md`](./notebooks/README.md)

### 2) Prerequisites
- Python 3.10+
- Jupyter Notebook or JupyterLab
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 3) Exact run order for notebooks
1. [`notebooks/01_intro_bike_demand_regression_instructor.ipynb`](./notebooks/01_intro_bike_demand_regression_instructor.ipynb)
2. [`notebooks/02_bike_demand_regression_advanced_extension.ipynb`](./notebooks/02_bike_demand_regression_advanced_extension.ipynb)
3. [`notebooks/03_challenge_bank_marketing_classification.ipynb`](./notebooks/03_challenge_bank_marketing_classification.ipynb)

Notebook run contract:
- run top-to-bottom from a clean kernel,
- keep paths relative to repo root,
- if internet is unavailable, pre-place cached CSVs in `data/`.

### 4) Challenge submission format
- Student submission CSV format: `id,y_prob`
- Template: [`templates/submission_template.csv`](./templates/submission_template.csv)

---

## Curriculum-first structure

```text
slides/       -> original slide deck
modules/      -> structured teaching notes aligned to slides
notebooks/    -> practical labs and challenge
competition/  -> instructor leaderboard scoring tooling
templates/    -> submission/label templates
docs/         -> release workflow
```

---

## Competition and fairness workflow

Public repo includes challenge notebook + submission template.  
Instructor-only assets (private labels, full solution bank) should remain private during competition.

Official winner ranking:
1. Primary: PR-AUC
2. Tie-breaker 1: F1 at threshold 0.50
3. Tie-breaker 2: lower log loss

Instructor scoring command:
```bash
python competition/competition_score_bank_marketing.py \
  --labels private_labels.csv \
  --submissions submissions \
  --out leaderboard.csv
```

Private label interface:
- `id,y_true` (see template: [`templates/private_labels_template.csv`](./templates/private_labels_template.csv))

---

## Two-phase release policy

- **v1.0-workshop**: full teaching content, challenge live, private solutions withheld.
- **v1.1-postworkshop**: publish full solutions + post-mortem notes after deadline.

Release details: [`docs/release_workflow.md`](./docs/release_workflow.md)

---

## Reuse this course

You can reuse this repo for future cohorts:
1. Fork the repo.
2. Update slide branding and examples.
3. Swap datasets and adjust notebook objectives.
4. Keep the same module + notebook sequence for consistent delivery.

Recommended maintenance:
- tag stable workshop versions (`v1.0-workshop`, `v1.1-postworkshop`, etc.),
- track updates in [`CHANGELOG.md`](./CHANGELOG.md),
- keep private grading assets out of public commits.

# IntroductionToML
