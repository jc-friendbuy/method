
class LineTrendFormatter(object):

    def __init__(self, line_color='blue', line_width=2):
        self._line_color = line_color
        self._line_width = line_width

    def format(self, x, y, plot):
        """
        Assumes plot is a matplotlib plot object.
        """
        return plot.plot(x, y, color=self._line_color, linewidth=self._line_width)
