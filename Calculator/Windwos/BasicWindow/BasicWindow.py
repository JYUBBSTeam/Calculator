from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QFile
import sys


class windows_static_data:
    width = 500
    height = 400
    top = 100
    left = 100


class UI_basic_window(QtWidgets):

    def __init__(self):
        # 读取qss文件
        qss_file = QFile("QSS/BasicStyle.qss")
        qss_file.open(QFile.ReadOnly)
        # 读取qss文件
        if qss_file.isOpen():
            qss_stream = QtCore.QTextStream(qss_file).readAll()
            self.setStylesheet(qss_stream)
        else:
            # 退出值为1说明打开qss失败
            sys.exit(1)

        self.setGeometry(windows_static_data.left, windows_static_data.top, windows_static_data.width,
                         windows_static_data.height)

    def set_button_location(self, button, x_ratio, y_ratio):
        
