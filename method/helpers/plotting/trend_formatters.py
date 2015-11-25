# All classes must implement the format(self, x, y, plot) method

class NoTrendFormatter(object):

    def __init__(self):
        pass

    def format(self, x, y, plot, **kwargs):
        return None

class LineTrendFormatter(object):

    def __init__(self, line_width=2):
        self._line_width = line_width

    def format(self, x, y, plot, line_color='blue', **kwargs):
        """
        Assumes plot is a matplotlib plot object.
        """
        return plot.plot(x, y, color=line_color, linewidth=self._line_width)
