# Module 4: Evaluation Metrics (Regression + Classification)
**Slide coverage:** 19-29

## Learning objectives
- Understand why evaluation is distinct from training.
- Interpret core regression metrics (MAE, MSE, RMSE).
- Interpret classification metrics using confusion-matrix components.

## Key formulas and concepts
- Regression:
  - `MAE = (1/n) * sum |y_i - y_hat_i|`
  - `MSE = (1/n) * sum (y_i - y_hat_i)^2`
  - `RMSE = sqrt(MSE)`
- Confusion matrix terms: `TP, TN, FP, FN`
- Classification:
  - `Accuracy = (TP + TN) / (TP + TN + FP + FN)`
  - `Precision = TP / (TP + FP)`
  - `Recall = TP / (TP + FN)`
  - `F1 = 2 * (Precision * Recall) / (Precision + Recall)`

## Teaching notes
- Stress metric-choice consequences:
  - False positives costly -> precision focus
  - False negatives costly -> recall focus
- Use F1 when balancing precision and recall is important.
- Tie metric selection to the real task, not to “highest accuracy by default.”

## What students should be able to do
- Choose a metric that matches business/operational cost.
- Read a confusion matrix and identify the dominant error type.
- Explain why RMSE penalizes large misses more than MAE.

