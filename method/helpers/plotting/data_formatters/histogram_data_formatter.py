
class HistogramDataFormatter(object):
    def __init__(self, face_color='white', grid=True):
        self._face_color = face_color
        self._grid = grid

    def format(self, x, bins, plot):
        """
        Assumes plot is a matplotlib plot object.
        """
        plot.grid(self._grid)
        return plot.hist(x, bins, color=self._face_color)
