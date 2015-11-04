
import unittest
import pytest
import numpy as np
from method.helpers.plot import Plot

"""
Tests for helpers/plot.py
"""

test_data = [
    ([1, 2, 3, 4, 5], [1.9, 3.7, 5.8, 8.0, 9.6])
]

@pytest.mark.parametrize("x,y", test_data)
def test_png_file_works(x, y):
    """
    Is the R^2 calculation for x and predicted equals to a known quantity that is correct?
    """
    plot = Plot()
    output = plot.scatter_2D(x, y).as_raw_png_binary_string()
    with open("/Users/jc/Desktop/out.png", "wb") as f:
        f.write(output.getvalue())
    output.close()
