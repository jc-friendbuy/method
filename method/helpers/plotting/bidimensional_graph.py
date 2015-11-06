# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.
# Plotting code will be here once the migration from R is complete.

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from io import BytesIO

class BidimensionalGraph(object):

    _DEFAULT_RESOLUTION_DPI = 150

    def __init__(self, data_formatter, trend_formatter):
        self._data_formatter = data_formatter
        self._trend_formatter = trend_formatter

        self._figure = None
        self._plot = None
        self._canvas = None
        self._initialize_graphics()

    def set_title(self, title):
        self._assert_graphics_is_initialized()
        self._plot.set_title(title)
        return self

    def set_xlabel(self, label):
        self._assert_graphics_is_initialized()
        self._plot.set_xlabel(label)
        return self

    def set_ylabel(self, label):
        self._assert_graphics_is_initialized()
        self._plot.set_ylabel(label)
        return self

    def add_data(self, x, y):
        self._data_formatter.format(x, y, self._plot)
        return self

    def add_trend(self, x, trend):
        self._trend_formatter.format(x, trend, self._plot)
        return self

    def as_raw_png_binary_string(self):
        output_string = BytesIO()
        self._canvas.print_png(output_string, dpi=self._DEFAULT_RESOLUTION_DPI)
        return output_string

    def reset(self):
        self._initialize_graphics()

    def _initialize_graphics(self):
        self._figure = Figure()
        self._plot = self._figure.add_subplot(1, 1, 1)
        self._canvas = FigureCanvasAgg(self._figure)

    def _assert_graphics_is_initialized(self):
        assert isinstance(self._figure, Figure)
        assert isinstance(self._plot, Axes)
        assert isinstance(self._canvas, FigureCanvasAgg)
