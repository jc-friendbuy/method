
import unittest
import pytest
import numpy as np
from method.model import goodness_of_fit
from test.common import assert_values_are_within_epsilon_distance

"""Tests for `model/goodness_of_fit.py`."""

test_data = [
    ([1, 2, 3, 4, 5], [1.9, 3.7, 5.8, 8.0, 9.6])
]

@pytest.mark.parametrize("observed,predicted", test_data)
def test_r2_equals_known_value(observed, predicted):
    """
    Is the R^2 calculation for x and predicted equals to a known quantity that is correct?
    """
    observed = np.array(observed, np.float64)
    predicted = np.array(predicted, np.float64)
    m = np.mean(observed, dtype=np.float64)
    total_sum_of_squares = np.sum(np.power(observed - m, 2))
    residual_sum_of_squares = np.sum(np.power(observed - predicted, 2))

    expected_value = 1 - (residual_sum_of_squares / total_sum_of_squares)
    calculated_value = goodness_of_fit.coefficient_of_determination(observed, predicted)
    assert_values_are_within_epsilon_distance(calculated_value, expected_value)
