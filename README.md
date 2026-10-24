# Code platform controlled fixture

This repository is a synthetic test fixture, not a customer application.

`src/pricing.py` exposes `final_price(price, discount)` for nonnegative integer
prices and fixed discounts. The result must never be below zero. Negative inputs
must raise ValueError. Ordinary inputs must preserve subtraction behavior.

The initial revision intentionally contains one boundary defect. A separate,
external oracle verifies the original and returned worktrees. Repository-local
test success alone is not the acceptance criterion.

Local validation: `python3 -m unittest discover -s tests -v`.
