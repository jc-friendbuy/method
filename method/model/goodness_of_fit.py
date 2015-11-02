# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.
# Measurements of goodness of fit.  These functions calculate a value that indicates a measure of
# distance between vectors.
import numpy as np
from sklearn.metrics import r2_score as _r2_score

def difference_of_squares(x, y):
    """
    Calculare the difference of the squares of both vectors.
    """
    _validate_arrays(x, y)
    return sum((x - y) ^ 2)

def coefficient_of_determination(observed, predicted):
    """
    Calculate the coefficient of determination (a.k.a. R^2) between both arrays (observed and
    predicted as usually called).
    """
    _validate_arrays(observed, predicted)
    return _r2_score(observed, predicted)

def _validate_arrays(x, y):
    """
    Assert that input arrays are ndarrays and their dimensions are equal (to support subtraction)
    """
    _assert_array_is_ndarray(x)
    _assert_array_is_ndarray(y)
    _assert_array_is_double_precision(x)
    _assert_array_is_double_precision(y)
    _assert_array_shapes_are_equivalent(x, y)

def _assert_array_is_ndarray(a):
    """
    Assert if an array is of datatype ndarray (numpy n-dimensional array).
    """
    assert isinstance(a, np.ndarray), "The input array is not ndarray."

def _assert_array_shapes_are_equivalent(a, b):
    """
    Assert that the shapes of both provided arrays are equivalent.
    """
    assert a.shape == b.shape, "The shapes of the input arrays are not equivalent."

def _assert_array_is_double_precision(a):
    assert a.dtype == np.float64, "The input array's data type is different from float64."
