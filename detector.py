"""A toy anomaly detector under test for the ZERO-false-positive question.

`is_anomaly(x)` flags a value as anomalous. The "zero false positive" idea is the
claim that it NEVER flags a legitimate (non-anomalous) input. Gates A-D probe this
on finite, known sets; gates E-F assert it over an unbounded/adversarial space.
"""

from __future__ import annotations

THRESHOLD = 0.90


def score(x: float) -> float:
    # Deliberately simple; the point of the scenario is the *claim*, not the model.
    return 1.0 / (1.0 + pow(2.718281828, -(x - 5.0)))


def is_anomaly(x: float) -> bool:
    return score(x) >= THRESHOLD
