"""
    创建基本窗口
"""

from PyQt5.QtWidgets import QApplication, QWidget, QSizeGrip, QVBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


class BasicCACLWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.basicCACLWindowTitle = "Deep Learning CACL"
        self.basicCACLWindowTop = 100
        self.basicCACLWindowLeft = 900
        self.basicCACLWindowWidth = 1000
        self.basicCACLWindowHeight = 900

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.basicCACLWindowTitle)
        self.setGeometry(self.basicCACLWindowLeft, self.basicCACLWindowTop, self.basicCACLWindowWidth,
                         self.basicCACLWindowHeight)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        vBox = QVBoxLayout()
        sizeGrip = QSizeGrip(self)
        vBox.addWidget(sizeGrip)

        self.setLayout(vBox)

        self.show()


# class CACLWindowsButton(QWidget):

basicApplication = QApplication(sys.argv)
basicWindow = BasicCACLWindow()

sys.exit(basicApplication.exec())
