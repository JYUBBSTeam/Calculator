# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
    @Project -> File  : Calculator -> runHistory
    @创建人：Liang
    @创建时间：2019/11/4
    @最后一次编辑时间：
    @描述：
    @类：
    @函数：
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Calculator.Sourse.Window.childWindow.calculatorWindow.UIdesigne.history import UiHistoryDialog


class History(QWidget, UiHistoryDialog):
    """
    加载历史记录窗口
    """

    def __init__(self):
        super(History, self).__init__()
        self.setup_ui(self)
        self.retranslate_ui(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    historyWin = History()
    historyWin.show()
    sys.exit(app.exec_())
