
import unittest
import pytest
import numpy as np
from method.helpers.plotting.bidimensional_graph import BidimensionalGraph
from method.helpers.plotting.data_formatters import ScatterDataFormatter
from method.helpers.plotting.trend_formatters import NoTrendFormatter
from contextlib import closing

"""
Tests for helpers/plot.py
"""

test_data = [
    ([1, 2, 3, 4, 5], [1.9, 3.7, 5.8, 8.0, 9.6])
]

@pytest.mark.parametrize("x,y", test_data)
def test_png_file_contents_match_png_image_data(x, y, tmpdir):
    """
    Is the R^2 calculation for x and predicted equals to a known quantity that is correct?
    """
    output_path = str(tmpdir.mkdir("out").join("scatter.png"))

    graphic = BidimensionalGraph(ScatterDataFormatter(), NoTrendFormatter())
    graphic.add_data(x, y)

    with closing(graphic.as_raw_png_binary_string()) as output_stream:
        output_stream_data = output_stream.getvalue()

    with open(output_path, "wb") as out_file:
        out_file.write(output_stream_data)

    with open(output_path, "rb") as in_file:
        file_contents = in_file.read()

    assert file_contents == output_stream_data
