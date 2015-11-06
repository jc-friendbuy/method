

class ScatterDataFormatter(object):
    def __init__(self, dot_color='black'):
        self._dot_color = dot_color

    def format(self, x, y, plot):
        """
        Assumes plot is a matplotlib plot object.
        """
        plot.scatter(x, y, color=self._dot_color)
