# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @Project -> File  : Calculator -> showCalculator
    @创建人：Liang
    @创建时间：2019/10/29
    @最后一次编辑时间：
    @描述：
    @类：
    @函数：
'''

import sys
from PyQt5.QtWidgets import QApplication
from Calculator.Sourse.Window.childWindow.calculatorWindow.calculator import calculator

# 测试
if __name__ == '__main__':
   app = QApplication(sys.argv)
   showCalculation = calculator()
   showCalculation.show()

   sys.exit(app.exec_())