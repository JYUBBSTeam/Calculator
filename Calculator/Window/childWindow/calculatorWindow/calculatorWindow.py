'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：计算器窗口界面
    类：
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget

from Calculator.Window.childWindow.calculatorWindow.calculator_setup_UI import setupUI
from Calculator.Window.childWindow.calculatorWindow.calculator_init_UI import init_UI
from Calculator.Window.loadQss.commomHelper_Qss import CommonHelper_qss

sys.setrecursionlimit(10000)


class calculator_Window(QWidget):
    '''
        计算器界面窗口
    '''
    def __init__(self) :
        super(calculator_Window, self).__init__()

        self.init_Ui()
        self.setup_Ui()

        self.show()

    def setup_Ui(self):
        self.setup_Win = setupUI.setup_Window(self)

    def init_Ui(self):
        self.init_Ui = init_UI.init_Ui(self)

#测试
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator_win = calculator_Window()
    # 加载Qss样式表
    #styleFile = '../../childWindow/calculatorWindow/Qss/calculatorWindow.qss'
    #qssStyle = CommonHelper_qss.readQss(styleFile)
    #calculator_win.setStyleSheet(qssStyle)
    calculator_win.show()

    sys.exit(app.exec_())

