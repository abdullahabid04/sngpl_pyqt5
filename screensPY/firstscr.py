# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screensUI/firstscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class FirstWin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 800, 600))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 110, 281, 251))
        self.label.setStyleSheet("image:url(:/Images/SNGPL-1.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget_frame = QtWidgets.QFrame(self.frame)
        self.widget_frame.setGeometry(QtCore.QRect(0, 420, 800, 150))
        self.widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widget_frame.setObjectName("widget_frame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))