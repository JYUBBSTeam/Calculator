# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @Project -> File  : Calculator -> showFunction
    @创建人：Liang
    @创建时间：2019/11/5
    @最后一次编辑时间：
    @描述：
    @类：
    @函数：
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Calculator.Sourse.UI.function import Ui_Form

class functionForm(QWidget, Ui_Form):
    def __init__(self):
        super(functionForm, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    functionWin = functionForm()
    functionWin.show()
    sys.exit(app.exec_())




