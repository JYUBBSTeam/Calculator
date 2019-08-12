'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：主窗口(创建菜单栏、状态栏、工具栏）
    类: mainWindow:主窗口
'''

from PyQt5.QtWidgets import QMainWindow, QFileDialog

from Calculator.Window.childWindow.calculatorWindow.calculatorWindow import calculator_Window
from Calculator.Window.mainWindow.mainWindow_setup_UI import setupUI
from Calculator.Window.mainWindow.mainWindow_init_UI import init_UI





class mainWindow(QMainWindow):
    '''
        主窗口
    '''
    def __init__(self):
        super(mainWindow, self).__init__()

        self.setup_Ui()
        self.init_Ui()

    def init_Ui(self):
        self.setup_Ui = init_UI.initUI(self)

    def setup_Ui(self):
        self.setupUi = setupUI.setup_Window(self)

    def getFile(self):
        '''
            getOpenFileName():返回用户所选择文件的名称，并打开该文件
            第一个参数用于指定父组件
            第二个参数指定对话框标题
            第三个参数指定目录
            第四个参数是文件扩展名过滤器
        '''

        fname = QFileDialog.getOpenFileName(self, '选择文件', 'C:\\', "*.jpg *.gif *.png")

    # 加载计算器窗口
    def calculator_Win(self):
        self.calculator_Win = calculator_Window()

        self.calculator_Win.show()


