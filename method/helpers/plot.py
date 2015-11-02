# Author and copyright: Juan Carlos Coto, 2015.  Usage under explicit instruction only.
# Plotting code will be here once the migration from R is complete.

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from io import BytesIO
from contextlib import closing

class Plot(object):

    _PNG_DPI = 150

    def __init__(self):
        self._figure = None
        self._plot = None
        self._canvas = None

    def _initialize_graphics(self):
        self._figure = Figure()
        self._plot = self._figure.add_subplot(1, 1, 1)
        self._canvas = FigureCanvasAgg(self._figure)

    def _assert_graphics_is_initialized(self):
        assert isinstance(self._figure, Figure)
        assert isinstance(self._plot, Axes)
        assert isinstance(self._canvas, FigureCanvasAgg)

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

    def scatter_2D(self, x, y, dot_color='black'):
        self._initialize_graphics()
        self._plot.scatter(x, y, color=dot_color)
        return self

    def line(self, x, y, line_color='blue', line_width=2):
        self._assert_graphics_is_initialized()
        self._plot.plot(x, y, color=line_color, linewidth=line_width)
        return self

    def as_raw_png_binary_string(self):
        output_string = BytesIO()
        self._canvas.print_png(output_string, dpi=self._PNG_DPI)
        return output_string
