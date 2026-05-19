# Module 3: Training Math (Features, Loss, Objective, Gradient Descent)
**Slide coverage:** 14-18

## Learning objectives
- Read standard supervised-learning notation.
- Connect predictions, loss, and optimization objective.
- Explain gradient descent update intuition.

## Key formulas and concepts
- Dataset notation: `D = {(x_1, y_1), ..., (x_n, y_n)}`
- Matrix view: `X in R^(n x d)`, `y in R^n`
- Model prediction: `y_hat = f_theta(x)`
- Loss function: `L(y, y_hat)`
- Empirical risk/objective:
  - `J(theta) = (1/n) * sum_{i=1..n} L(y_i, f_theta(x_i))`
- Gradient update:
  - `theta := theta - alpha * grad_theta J(theta)`

## Teaching notes
- Keep intuition strong: we optimize parameters to reduce average training error.
- Explain `alpha` (learning rate) as step size control.
- Highlight that different model families share the same optimize-loss pattern.

## What students should be able to do
- Interpret each symbol in the training objective.
- Explain why minimizing `J(theta)` is central to model training.
- Describe what happens if learning rate is too small or too large.

