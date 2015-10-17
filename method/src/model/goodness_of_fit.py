# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.
# Measurements of goodness of fit.  These functions calculate a value that indicates a measure of
# distance between vectors.
from numpy import ndarray
from sklearn.metrics import r2_score as _r2_score

# Calculare the difference of the squares of both vectors.
def difference_of_squares(x, y):
    _assert_vectors_are_ndarray_and_dimensions_are_compatible(x, y)
    return sum((x - y) ^ 2)

# Calculate the coefficient of determination between both vectors (a.k.a. R^2)
def coefficient_of_determination(x, y):
    _assert_vectors_are_ndarray_and_dimensions_are_compatible(x, y)
    return _r2_score(x, y)

# Assert that input arrays are ndarrays and their dimensions are equal (to support subtraction)
def _assert_vectors_are_ndarray_and_dimensions_are_compatible(x, y):
    assert isinstance(ndarray, x) and isinstance(ndarray, y) and x.shape == y.shape,
        "Both input vectors must be numpy ndarrays of equal dimension"
