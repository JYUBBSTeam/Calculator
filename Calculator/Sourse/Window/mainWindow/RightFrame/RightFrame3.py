# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: RightFrame1.py
    @date: 2020/2/26
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/2/26
-----------------------------------
    @desc:
    
----------------------------------- 
"""

from PyQt5.QtWidgets import QWidget, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QFont


class RightForm3(QWidget):
    def __init__(self):
        super(RightForm3, self).__init__()
        self.setup_ui()
        self.set_form_layout()

    def init(self):
        pass

    def setup_ui(self):
        self.notice = QTextEdit()
        self.notice.setReadOnly(True)
        self.notice.setText("本模块还没开发")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        self.notice.setFont(font)

    def set_form_layout(self):
        all_layout = QHBoxLayout()

        self.setLayout(all_layout)

        all_layout.addWidget(self.notice)

