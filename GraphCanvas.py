import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        matplotlib.rc('font', size=8)

        self.fig = Figure()
        self.plot = self.fig.add_subplot(111)

        super(MplCanvas, self).__init__(self.fig)

        self.fig.tight_layout()

        self.plot.spines["top"].set_visible(False)
        self.plot.spines["right"].set_visible(False)

        self.plot.spines["bottom"].set_color("#1e1953")
        self.plot.spines["left"].set_color("#1e1953")

        self.plot.tick_params(axis='x', colors="#1e1953")
        self.plot.tick_params(axis='y', colors="#1e1953")
