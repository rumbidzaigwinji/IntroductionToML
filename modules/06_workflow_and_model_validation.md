# Module 6: Workflow and Model Validation
**Slide coverage:** 33-35

## Learning objectives
- Describe an end-to-end ML workflow.
- Distinguish train, validation, and test roles.
- Recognize overfitting and underfitting patterns.

## Key formulas and concepts
- Standard split concept:
  - Train set: learn parameters
  - Validation set: tune/compare models
  - Test set: final unbiased estimate
- Overfitting signal: strong train performance, weaker generalization.
- Underfitting signal: poor train and test performance.

## Teaching notes
- Keep “do not tune on the test set” as a hard rule.
- Show that model complexity is a tradeoff:
  - too simple -> underfit
  - too complex -> overfit
- Connect workflow to the practical notebooks students run next.

## What students should be able to do
- Explain the purpose of each data split.
- Spot basic overfit/underfit symptoms from metric comparisons.
- Outline a minimal, repeatable ML workflow from raw data to final evaluation.

