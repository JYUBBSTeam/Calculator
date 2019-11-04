# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @Project -> File  : Calculator -> runHistory
    @创建人：Liang
    @创建时间：2019/11/4
    @最后一次编辑时间：
    @描述：
    @类：
    @函数：
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Calculator.Sourse.Window.childWindow.calculatorWindow.history import Ui_history_Dialog

class history(QWidget, Ui_history_Dialog):
    def __init__(self):
        super(history, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    historyWin = history()
    historyWin.show()
    sys.exit(app.exec_())