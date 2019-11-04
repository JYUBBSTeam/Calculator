# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @创建人：Liang
    @创建时间：2019/7/18
    @最后一次编辑时间：
    @描述：主窗口
    @类: mainWindow:主窗口
    @函数：
'''

import const
from PyQt5.QtWidgets import QMenu, QMainWindow, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from Calculator.Sourse.Window.childWindow.calculatorWindow.calculatorMainWindow import calculatorMainWindow
from Calculator.Sourse.Window.mainWindow.QAction.qAction import Action

const.WIN_X = 250
const.WIN_Y = 150
const.WIN_WIDTH = 1400
const.WIN_HEIGHT = 750



class mainWindow(QMainWindow):
    '''
        主窗口
    '''
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setGeometry(const.WIN_X, const.WIN_Y, const.WIN_WIDTH, const.WIN_HEIGHT)
        self.setObjectName('mainWindow')
        self.setWindowIcon(QIcon("./image/history.jpg"))
        self.setWindowTitle('智能公式识别IFR')
        self.setup_UI()
        self.createContextMenu()

    def setup_UI(self):
        '''
            创建状态栏、菜单栏、工具栏
        '''

        # 设置状态栏
        self.statusBar().showMessage('准备就绪', 5000)


        ################################################################################################################

        self.menubar = self.menuBar()

        # 文件
        fileMenu = self.menubar.addMenu('&文件(F)')

        # 调用自定义action
        openPimax = Action.action_3_b(self, 'openPimax', '&打开图片文件', 'Ctrl+P', '打开图片文件')
        openPimax.setIcon(QIcon('./image/openQpixmap.jpg'))
        openText = Action.action_3_b(self, 'openText', '&打开文本文件', 'Ctrl+T', '打开文本文件')
        openText.setIcon(QIcon('./image/openText.ico'))
        # openFile = Action.action_1(self, 'openFile', './image/openFile.jpg', '&打开文件', 'O', '打开文件', fileMenu)
        openFile = Action.action_3_c(self, 'openFile', '打开文件', '打开文件', fileMenu)
        openFile.addAction(openPimax)
        openFile.addAction(openText)

        openPimax.triggered.connect(lambda: self.getFile())
        openText.triggered.connect(lambda: self.getText())
        openRecentFile = Action.action_2(self, 'openRecentFile', '&最近打开的文件', 'Ctrl+O', '最近打开的文件', fileMenu)
        # openRecentFile.triggered.connect(self.)
        save = Action.action_2(self, 'save', '&保存分析结果', 'Ctrl+S', '保存数据分析结果', fileMenu)
        # save.triggered.connect(self.)
        saveAs = Action.action_2(self, 'saveAs', '&另保存分析结果', 'Ctrl+Shift+S', '另保存数据分析结果', fileMenu)
        # saveAs.triggered.connect(self.)
        printf = Action.action_2(self, 'printef', '&打印分析结果', 'Ctrl+P', '打印数据分析结果', fileMenu)
        # printf.triggered.connect(self.)
        exitAction = Action.action_1(self, 'exitAction', './image/Exit.jpg', '&退出', 'Ctrl+Q', '退出应用程序', fileMenu)
        exitAction.triggered.connect(self.close)

        # 编辑
        exitMenu = self.menubar.addMenu('&编辑(E)')
        #
        ####################查找与替换####################开始
        search = Action.action_3_b(self, 'search', '&快速查找', 'Ctrl+F', '快速查找')
        replace = Action.action_3_b(self, 'replace', '&快速替换', 'Ctrl+H', '快速替换')

        # 新增二级菜单
        searchAndReplaceMenu = Action.action_3_c(self, 'searchAndReplaceMenu', '查找与替换', '查找与替换', exitMenu)
        searchAndReplaceMenu.addAction(search)
        searchAndReplaceMenu.addAction(replace)

        # search.triggered.connect(self.)
        # replace.triggered.connect(self.)

        # ####################查找与替换####################结束

        cut = Action.action_2(self, 'cut', '&剪切', 'Ctrl+X', '剪切', exitMenu)
        # cut.triggered.connect(self.)
        copy = Action.action_2(self, 'copy', '&复制', 'Ctrl+C', '复制', exitMenu)
        # copy.triggered.connect(self.)
        paste = Action.action_2(self, 'paste', '&粘贴', 'Ctrl+V', '粘贴', exitMenu)
        # paste.triggered.connect(self.)
        delete = Action.action_2(self, 'delect', '&删除', 'Del', '删除', exitMenu)
        # delect.triggered.connect(self.)
        selectAll = Action.action_2(self, 'selectAll', '&全选', 'Ctrl+Alt', '全选', exitMenu)
        # selectAll.triggered.connect(self.)

        # # 视图
        viewMenu = self.menubar.addMenu('&视图(V)')

        notice = Action.action_2(self, 'notice', '&通知', 'Ctrl+Alt+X', '信息通知提醒', viewMenu)
        # notice.triggered.connect(self.)

        ####################窗口管理####################开始
        window = Action.action_3_c(self, 'window', '&窗口', '展示一些基本窗口', viewMenu)

        ####################窗口管理####################结束
        #
        #
        #
        ####################工具栏####################开始
        tool = Action.action_3_c(self, 'tool', '&工具栏', '基本工具', viewMenu)

        calculator = Action.action_1(self, 'calculator', './image/calculator.jpg', '&计算器', 'C', '计算器', viewMenu)
        calculator.triggered.connect(self.calculator_Win)

        ####################工具栏####################结束
        fullScreen = Action.action_2(self, 'fullScreen', '&全屏幕', 'Shift+Alt+Enter', '全屏', viewMenu)
        # fullScreen.triggered.connect(self.)
        propertyWindow = Action.action_2(self, 'propertyWindow', '&属性窗口', 'F4', '属性窗口', viewMenu)
        # propertyWindow.triggered.connect(self.)
        #

        # 分析
        navigateMenu = self.menubar.addMenu('&分析(N)')
        #

        # 工具
        toolMenu = self.menubar.addMenu('&工具(T)')
        #

        # 扩展
        extendMenu = self.menubar.addMenu('&扩展(X)')
        #

        # 窗口
        windowMenu = self.menubar.addMenu('&窗口(W)')
        #

        # 帮助
        helpMenu = self.menubar.addMenu('&帮助(H)')

        help = Action.action_2(self, 'help ', '&查看帮助', 'Ctrl+F1', '查看帮助', helpMenu)
        # help.triggered.connect(self.)
        ####################菜单栏####################结束

        ################################################################################################################

        ####################工具栏####################开始
        # 工具

        self.pixmapToolbar = self.addToolBar('打开图形文件')
        self.textToolbar = self.addToolBar('打开文本文件')
        self.pixmapToolbar.addAction(openPimax)
        self.textToolbar.addAction(openText)

        self.exitToolbar = self.addToolBar('退出')
        self.exitToolbar.addAction(exitAction)

        self.calculatorTooolbar = self.addToolBar('计算器')
        self.calculatorTooolbar.addAction(calculator)

        ####################工具栏####################结束

    # 加载计算器窗口
    def calculator_Win(self):
        self.calculator_Win = calculatorMainWindow()
        self.calculator_Win.show()

    ######################################################################################
    #                                   右键菜单
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
        self.closeAction.triggered.connect(self.QuitWindow)
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


    # 最小化窗口
    def ShowMininizedWindow(self):
        self.showMinimized()

    # 最大化窗口
    def ShowMaximizedWindow(self):
        self.showMaximized()

    # 复原窗口
    def ShowRestoreWindow(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # 关闭窗口
    def QuitWindow(self):
        self.QuitWindow(self)

    # 打开文件
    def getFile(self):
        pass
        '''
            getOpenFileName():返回用户所选择文件的名称，并打开该文件
            第一个参数用于指定父组件
            第二个参数指定对话框标题
            第三个参数指定目录
            第四个参数是文件扩展名过滤器
        '''

        # fname, _ = QFileDialog.getOpenFileName(self, '选择图形文件', 'C:\\', "*.jpg *.gif *.png")
        # self.pixmapLabel.setPixmap(QPixmap(fname))

    def getText(self):
        pass
        # # 初始化实例，并设置一些参数
        # # textDialog = QFileDialog()
        # # textDialog.setFileMode(QFileDialog.AnyFile)
        # # textDialog.setFilter(QDir.Files)
        # textDialog = QFileDialog.getOpenFileName(self, '选择文本文件', 'C:\\', "*.txt *.doc *.docx")
        # # 当选择器关闭的时候
        # if textDialog.exec_():
        #     # 拿到所选择的文本
        #     filenames = textDialog.selectedFiles()
        #     # 读取文本内容设置到textEdit中
        #     f = open(filenames[0], 'r')
        #     with f:
        #         data = f.read()
        #         self.textEdit.setText(data)



