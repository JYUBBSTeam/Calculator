# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @Project -> File  : Calculator -> quitWarmming
    @创建人：Liang
    @创建时间：2019/11/4
    @最后一次编辑时间：
    @描述：
    @类：
    @函数：
'''

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QVBoxLayout
from PyQt5.QtGui import QPixmap

class quitWarmming(QWidget):
    def __init__(self):
        super(quitWarmming, self).__init__()
        self.resize(300, 250)
        self.setObjectName('quitWarmming')
        self.setupUI('','', '确认退出吗？')

    def setupUI(self, self_1, icon, text):
        self.iconLabel = QLabel(self)
        self.iconLabel.setObjectName('iconLabel')
        self.iconLabel.setPixmap(QPixmap(icon))
        self.textLabel = QLabel(self)
        self.textLabel.setObjectName('textLabel')
        self.textLabel.setText(text)
        AllLayout = QVBoxLayout(self)
        AllLayout.setObjectName('AllLayout')

        self.quitPushButton = QPushButton('退出')
        self.quitPushButton.setObjectName('quitPushButton')
        self.cancelButton = QPushButton('取消')
        self.cancelButton.setObjectName('cancerButton')
        self.quitPushButton.clicked.connect(self.Quit)

        AllLayout.addWidget(self.textLabel)
        AllLayout.addWidget(self.iconLabel)

        AllLayout.addWidget(self.quitPushButton)
        AllLayout.addWidget(self.cancelButton)

    def Quit(self):
        self.close()

    def cancel(self):
        self.close()

# 测试
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    quitWindow = quitWarmming()
    quitWindow.show()
    sys.exit(app.exec_())
