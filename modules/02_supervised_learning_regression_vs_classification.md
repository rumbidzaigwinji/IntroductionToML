# Module 2: Supervised Learning (Regression vs Classification)
**Slide coverage:** 8-13

## Learning objectives
- Differentiate regression outputs from classification outputs.
- Interpret classification as probability estimation.
- Recognize binary vs multiclass settings.

## Key formulas and concepts
- Regression prediction: `y_hat = f(x)`
- Simple linear regression: `y_hat = w x + b`
- Regression error per sample: `error_i = y_i - y_hat_i`
- Classification output space:
  - Binary: `y_hat in {0, 1}`
  - Multiclass: `y_hat in {1, ..., K}`
- Probabilistic view: `P(y = 1 | x)`

## Teaching notes
- Emphasize output type first:
  - Continuous numeric value -> regression
  - Category/label -> classification
- Use threshold intuition for binary classification probabilities.
- Contrast business decisions from regression (quantity forecasts) vs classification (yes/no action).

## What students should be able to do
- Map a real-world problem to regression or classification correctly.
- Explain what a 0.87 class probability means operationally.
- Distinguish when binary versus multiclass formulations apply.

