"""Tiny statistics helpers used to practice the PR workflow.

Keep this module deliberately small: the point of the repo is the
branch -> commit -> PR -> CI -> review -> merge loop, not the math.
"""

from __future__ import annotations

from collections.abc import Iterable


def _as_floats(values: Iterable[float]) -> list[float]:
    return [float(v) for v in values]


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean.

    Raises:
        ValueError: if ``values`` is empty.
    """
    data = _as_floats(values)
    if not data:
        raise ValueError("mean() requires at least one value")
    return sum(data) / len(data)


def median(values: Iterable[float]) -> float:
    """Return the median.

    Raises:
        ValueError: if ``values`` is empty.
    """
    data = sorted(_as_floats(values))
    if not data:
        raise ValueError("median() requires at least one value")
    mid = len(data) // 2
    if len(data) % 2:
        return data[mid]
    return (data[mid - 1] + data[mid]) / 2


def clamp(value: float, low: float, high: float) -> float:
    """Clamp ``value`` into the inclusive range ``[low, high]``.

    Raises:
        ValueError: if ``low > high``.
    """
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(value, high))
