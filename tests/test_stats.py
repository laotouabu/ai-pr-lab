import pytest

from calc.stats import clamp, mean, median


def test_mean_basic():
    assert mean([1, 2, 3]) == pytest.approx(2.0)


def test_mean_accepts_generator():
    assert mean(x for x in [2, 4, 6]) == pytest.approx(4.0)


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([4, 1, 3, 2]) == 2.5


def test_median_empty_raises():
    with pytest.raises(ValueError):
        median([])


def test_clamp_inside():
    assert clamp(5, 0, 10) == 5


def test_clamp_below_and_above():
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10


def test_clamp_invalid_range():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)
