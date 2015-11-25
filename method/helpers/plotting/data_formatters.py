
class ScatterDataFormatter(object):
    def __init__(self, dot_color='black'):
        self._dot_color = dot_color

    def format(self, x, y, plot, **kwargs):
        """
        Assumes plot is a matplotlib plot object.
        """
        return plot.scatter(x, y, color=self._dot_color)

class HistogramDataFormatter(object):
    def __init__(self, face_color='white', grid=True):
        self._face_color = face_color
        self._grid = grid

    def format(self, x, y, plot, **kwargs):
        """
        Assumes plot is a matplotlib plot object.
        """
        plot.grid(self._grid)
        return plot.hist(x, y, color=self._face_color)
