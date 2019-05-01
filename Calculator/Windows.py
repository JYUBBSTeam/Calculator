"""
    创建基本窗口
"""

from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class BasicCACLWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.basicCACLWindowTitle = "Deep Learning CACL"
        self.basicCACLWindowTop = 100
        self.basicCACLWindowLeft = 100
        self.basicCACLWindowWidth = 400
        self.basicCACLWindowHeight = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.basicCACLWindowTitle)
        self.setGeometry(self.basicCACLWindowLeft, self.basicCACLWindowTop, self.basicCACLWindowWidth,
                         self.basicCACLWindowHeight)

        self.show()

basicApplication = QApplication(sys.argv)
basicWindow = BasicCACLWindow()

sys.exit(basicApplication.exec())