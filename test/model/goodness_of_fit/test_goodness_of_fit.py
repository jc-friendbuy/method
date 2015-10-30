
import unittest
import pytest
from numpy import ndarray
from method.model import goodness_of_fit

class GoodnessOfFitTestCase(unittest.TestCase):
    """Tests for `model/goodness_of_fit.py`."""

    test_data = [
        (ndarray([1, 2, 3, 4, 5]), ndarray([1, 4, 9, 16, 25]))
    ]

    @pytest.mark.parametrize("x, y", test_data)
    def test_r2_equals_known_value(self, x, y):
        """Is the R^2 calculation for x and y equals to a known quantity that is correct?"""
        mean_x = x.mean(dtype=np.float64)
        expected_value = sum((y - m) ^ 2) / sum((x - m) ^ 2)
        self.assertEquals(goodness_of_fit.coefficient_of_determination(x, y), expected_value)
