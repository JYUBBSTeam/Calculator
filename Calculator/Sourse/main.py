# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: main.py
    @date: 2019/7/18
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/2/23
-----------------------------------
    @desc:

-----------------------------------
"""

import sys
import cgitb
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, qApp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QImage
from Calculator.Sourse.Window.mainWindow.mainWindow import MainWindow
from Calculator.Sourse.Window.mainWindow.StartFace.StartFace import SplashScreen


def load_message(splash):
    """
    启动界面过程加载
    :param splash:
    :return:
    """
    count = 0
    load_str = '正在加载...%'
    for i in range(1001):

        if i % 10 == 0:
            splash.showMessage(load_str + str(count), Qt.AlignCenter, Qt.yellow)
            count += 1

        splash.update()


class Main(MainWindow):
    """
    程序启动类
    """

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)


    def closeEvent(self, event):
        """

        :param event:
        :return:
        """
        close_state = QMessageBox.information(self, '提示', '是否退出程序？', QMessageBox.Yes | QMessageBox.No)
        if close_state == QMessageBox.Yes:
            try:
                event.accept()
            except Exception as e:
                print(e)
        else:
            event.ignore()


if __name__ == "__main__":
    sys.excepthook = cgitb.enable(1, None, 5, '')
    app = QApplication(sys.argv)

    # # 定义启动界面字体格式
    # font = QFont()
    # font.setPointSize(16)
    # font.setBold(True)
    # font.setWeight(75)
    #
    # # 启动界面背景图片
    # img = QImage('./image/startBackground.jpg')
    # pixmap = QPixmap.fromImage(img.scaled(900, 600, Qt.IgnoreAspectRatio))
    # # 加载启动界面
    # splash = SplashScreen()
    # splash.setPixmap(pixmap)
    # splash.setFont(font)
    # splash.show()
    # load_message(splash)
    # qApp.processEvents()

    win = Main()
    win.showMaximized()

    # # 结束启动页
    # splash.finish(win)
    # # 释放变量
    # del font
    # del img
    # del pixmap

    sys.exit(app.exec_())
