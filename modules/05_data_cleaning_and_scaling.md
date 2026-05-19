# Module 5: Data Cleaning and Scaling
**Slide coverage:** 30-32

## Learning objectives
- Explain why data cleaning precedes model training.
- Identify common missing-value handling strategies.
- Understand feature scaling and when it helps.

## Key formulas and concepts
- Standardization (z-score): `z = (x - mu) / sigma`
- Min-max normalization:
  - `x' = (x - x_min) / (x_max - x_min)`

## Teaching notes
- Link data quality directly to model quality: “poor data -> poor model.”
- Discuss common missing-value options:
  - drop rows/columns,
  - impute with central tendency,
  - impute by group/context.
- Explain that scaling is crucial for many distance/gradient-based models.

## What students should be able to do
- Justify a simple missing-data strategy.
- Explain when scaling likely changes model behavior.
- Identify models where one-hot encoding and scaling are common preprocessing steps.

