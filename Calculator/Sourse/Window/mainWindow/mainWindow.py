'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：主窗口(创建菜单栏、状态栏、工具栏）
    类: mainWindow:主窗口
    函数：
'''


from PyQt5.QtWidgets import QMenu
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QCursor

from Calculator.Calculator.Sourse.Window.childWindow.calculatorWindow.calculatorWindow import calculator_Window
from Calculator.Calculator.Sourse.Window.mainWindow.mainWindow_init_UI import init_UI
from Calculator.Calculator.Sourse.Window.mainWindow.QAction.qAction import Action
from Calculator.Calculator.Sourse.Window.mainWindow.Function.mainWindow_function import function


class mainWindow(function):
    '''
        主窗口
    '''
    def __init__(self):
        super(mainWindow, self).__init__()

        self.setWindowIcon(QIcon("./image/history.jpg"))
        self.setWindowTitle('智能公式识别IFR')
        self.createContextMenu()
        self.setup_Window()
        self.init_Ui()

    def init_Ui(self):
        self.setup_Ui = init_UI.initUI(self)

    # 加载计算器窗口
    def calculator_Win(self):
        self.calculator_Win = calculator_Window()

        self.calculator_Win.show()



    ######################################################################################
    #
    #                                   右键菜单
    #
    ######################################################################################

    def createContextMenu(self):
        '''
            创建右键菜单
            :return:
        '''
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        # 创建QMenu
        self.contextMenu = QMenu(self)

        ####################工具栏管理####################开始
        self.toolBarManagementMenu = Action.action_3_d(self, 'toolBarManagementMenu', '&工具栏管理', self.contextMenu)
        # 未完成
        ####################工具栏管理####################结束
        self.restoreAction = Action.action_1(self, 'restoreAction',  './image/restore.png', '&复原', 'Win+shift+M', '复原窗口大小', self.contextMenu)
        self.minAtion = Action.action_1(self, 'minAcion', './image/min.png', '&最小化', 'Ctrl+M', '最小化窗口', self.contextMenu)
        self.maxAction = Action.action_1(self, 'maxAction', './image/max.png', '&全屏', 'F11', '全屏，最大化窗口', self.contextMenu)

        self.contextMenu.addSeparator()  # 添加分隔线

        self.cutAction = Action.action_2(self, 'cutAction', '&剪切', 'Ctrl+X', '剪切', self.contextMenu)
        self.copyAction = Action.action_2(self, 'copyAction', '&复制', 'Ctrl+C', '复制', self.contextMenu)
        self.pasteAction = Action.action_2(self, 'pasteAction', '&粘贴', 'Ctrl+V', '粘贴', self.contextMenu)
        self.deleteAction = Action.action_2(self, 'delectAction', '&删除', 'Del', '删除', self.contextMenu)
        self.selectAllAction = Action.action_2(self, 'selectAllAction', '&全选', 'Ctrl+Alt', '全选', self.contextMenu)

        self.contextMenu.addSeparator()  # 添加分隔线

        self.closeAction = Action.action_1(self, 'closeAction', './image/Exit.png', '&退出', 'Ctrl+W', '退出',self.contextMenu)

        self.restoreAction.triggered.connect(self.ShowRestoreWindow)
        self.minAtion.triggered.connect(self.ShowMininizedWindow)
        self.maxAction.triggered.connect(self.ShowMaximizedWindow)
        self.closeAction.triggered.connect(self.CloseWindow)
        # self.selectAllAction.triggered.connect(self.)
        # self.cutAction.triggered.connect(self.)
        # self.copyAction.triggered.connect(self.)
        # self.pasteAction.triggered.connect(self.)
        # self.delectAction.triggered.connect(self.)

    def showContextMenu(self):
        '''
            右键点击时调用的函数
            :return:
        '''
        # 显示菜单前，将它移动到鼠标点击的位置
        self.contextMenu.exec_(QCursor.pos())


