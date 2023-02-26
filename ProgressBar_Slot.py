from PyQt5 import QtCore
class ProgressBar(QtCore.QRunnable):
    def __init__(self, progressbar):
        QtCore.QRunnable.__init__(self)
        self.progressbar = progressbar
        
    def update(self,value):
        QtCore.QMetaObject.invokeMethod(self.progressbar, "setValue",
                                 QtCore.Qt.QueuedConnection,
                                 QtCore.Q_ARG(int, value))