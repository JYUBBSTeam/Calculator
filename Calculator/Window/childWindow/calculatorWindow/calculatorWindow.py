'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：计算器窗口界面
    类：
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from Calculator.Window.childWindow.calculatorWindow.calculator_setup_UI import setupUI
from Calculator.Window.childWindow.calculatorWindow.calculator_init_UI import init_UI
from Calculator.Window.commomHelper_init_Win.commomHelper_init_Win import CommonHelper_titleBar, CommomHelper_Window    #加载自定义标题栏的类、自定义窗口拖放和缩放功能的类
from Calculator.Window.commomHelper_loadQss.commomHelper_Qss import CommonHelper_qss

sys.setrecursionlimit(10000)


class calculator_Window(QWidget):
    '''
        计算器界面窗口
    '''
    def __init__(self) :
        super(calculator_Window, self).__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)     #设置无边框
        self.initWin = CommomHelper_Window()    #自定义移动和缩放功能

        #布局
        AllLayout = QVBoxLayout()
        AllLayout.setSpacing(0)
        AllLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(AllLayout)

        self.title = CommonHelper_titleBar()

        centerWidget = QWidget()
        AllLayout.addWidget(self.title)
        AllLayout.addWidget(centerWidget)

        centerWidget.initUi = calculator_Window.init_Ui(centerWidget)
        centerWidget.setupUi = calculator_Window.setup_Ui(centerWidget)

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

