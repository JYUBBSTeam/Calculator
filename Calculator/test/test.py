# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @Project -> File  : Calculator -> test
    @创建人：Liang
    @创建时间：2019/11/18
    @最后一次编辑时间：
    @描述：
    @类：
    @函数：
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QHBoxLayout

class Win(QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.layout = QHBoxLayout(self)
        self.text = QTextEdit(self)

        self.btn_1 = QPushButton('1', self)
        self.btn_1.clicked.connect(self.settext)

        self.btn_2 = QPushButton('2', self)
        self.btn_2.clicked.connect(self.settext)

        self.btn_3 = QPushButton('3', self)
        self.btn_3.clicked.connect(self.settext)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.btn_1)
        self.layout.addWidget(self.btn_2)
        self.layout.addWidget(self.btn_3)


    def settext(self):
        # self.sender_Text = self.sender().text()
        # self.text.setText(self.sender_Text)
        string = ['0', 'wi', '66']
        # string_1 = str(string)
        string_1 = ''.join(string)

        self.text.setText(string_1)



if __name__ == '__main__':
    app =QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())