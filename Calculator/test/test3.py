# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: test3.py
    @date: 2020/3/13
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/3/13
-----------------------------------
    @desc:
        QSplitter实现控件能拖动大小
----------------------------------- 
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt


class win(QWidget):
    def __init__(self):
        super(win, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        # 布局
        hbox = QHBoxLayout()

        frame1 = QFrame()
        frame2 = QFrame()
        frame3 = QFrame()

        frame1.setFrameShape(QFrame.StyledPanel)
        frame2.setFrameShape(QFrame.StyledPanel)
        frame3.setFrameShape(QFrame.StyledPanel)

        # 分隔符创建
        splitter1 = QSplitter(Qt.Horizontal)
        splitter2 = QSplitter(Qt.Vertical)

        splitter1.addWidget(frame1)
        splitter1.addWidget(frame2)

        splitter2.addWidget(splitter1)
        splitter2.addWidget(frame3)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = win()
    window.show()

    sys.exit(app.exec_())
