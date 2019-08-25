'''
    创建人：Liang
    创建时间：2019/7/25
    最后一次编辑时间：
    描述：窗口UI设计
    类: setupUI:主窗口UI设计
    函数：
'''

from PyQt5.QtWidgets import QAction, QMenu
from PyQt5.QtGui import QIcon


class setupUI:
    '''
        主窗口UI设置
    '''

    def setup_Window(self):
        '''
            创建状态栏、菜单栏、工具栏
        '''

        # textEdit = QTextEdit()
        # self.setCentralWidget(textEdit)

        # 设置状态栏
        self.statusBar().showMessage('准备就绪', 5000)

        ####################菜单栏####################开始
        self.menubar = self.menuBar()

        # 文件
        fileMenu = self.menubar.addMenu('&文件(F)')

        openFile = QAction(QIcon('./QIcon/openFile.jpg'), '&打开文件', self)
        openFile.setShortcut('O')
        openFile.setStatusTip('打开文件')
        fileMenu.addAction(openFile)
        # openFile.triggered.connect(mainWindow.getFile(self))

        openRecentFile = QAction('&最近打开的文件', self)
        openRecentFile.setShortcut('Ctrl+O')
        openRecentFile.setStatusTip('最近打开的文件')
        fileMenu.addAction(openRecentFile)
        # openRecentFile.triggered.connect(self.)

        save = QAction('&保存分析结果', self)
        save.setShortcut('Ctrl+S')
        save.setStatusTip('保存数据分析结果')
        fileMenu.addAction(save)
        # save.triggered.connect(self.)

        saveAs = QAction('&另保存分析结果', self)
        saveAs.setShortcut('Ctrl+Shift+S')
        saveAs.setStatusTip('另保存数据分析结果')
        fileMenu.addAction(saveAs)
        # saveAs.triggered.connect(self.)

        printf = QAction('&打印分析结果', self)
        printf.setShortcut('Ctrl+P')
        printf.setStatusTip('打印数据分析结果')
        fileMenu.addAction(printf)
        # printf.triggered.connect(self.)

        exitAction = QAction(QIcon('./QIcon/Exit.jpg'), '&退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出应用程序')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # 编辑
        exitMenu = self.menubar.addMenu('&编辑(E)')

        ####################查找与替换####################开始
        # 二级菜单下命令属性设置
        search = QAction('&快速查找', self)
        search.setShortcut('Ctrl+F')
        search.setStatusTip('快速查找')
        replace = QAction('&快速替换', self)
        replace.setShortcut('Ctrl+H')
        replace.setStatusTip('快速替换')

        # 新增二级菜单
        searchAndReplaceMenu = QMenu('查找与替换', self)
        searchAndReplaceMenu.setStatusTip('查找与替换')
        searchAndReplaceMenu.addAction(search)
        searchAndReplaceMenu.addAction(replace)

        # search.triggered.connect(self.)
        # replace.triggered.connect(self.)

        exitMenu.addMenu(searchAndReplaceMenu)
        ####################查找与替换####################结束

        cut = QAction('&剪切', self)
        cut.setStatusTip('剪切')
        cut.setShortcut('Ctrl+X')
        exitMenu.addAction(cut)
        # cut.triggered.connect(self.)

        copy = QAction('&复制', self)
        copy.setStatusTip('复制')
        copy.setShortcut('Ctrl+C')
        exitMenu.addAction(copy)
        # copy.triggered.connect(self.)

        paste = QAction('&粘贴', self)
        paste.setStatusTip('粘贴')
        paste.setShortcut('Ctrl+V')
        exitMenu.addAction(paste)
        # paste.triggered.connect(self.)

        delete = QAction('&删除', self)
        delete.setStatusTip('删除')
        delete.setShortcut('Del')
        exitMenu.addAction(delete)
        # delect.triggered.connect(self.)

        selectAll = QAction('&全选', self)
        selectAll.setStatusTip('全选')
        selectAll.setShortcut('Ctrl+Alt')
        exitMenu.addAction(selectAll)
        # selectAll.triggered.connect(self.)

        # 视图
        viewMenu = self.menubar.addMenu('&视图(V)')

        notice = QAction('&通知', self)
        notice.setShortcut('Ctrl+Alt+X')
        notice.setStatusTip('信息通知提醒')
        viewMenu.addAction(notice)
        # notice.triggered.connect(self.)

        ####################窗口管理####################开始
        window = QMenu('&窗口', self)
        window.setStatusTip('展示一些基本窗口')
        viewMenu.addMenu(window)

        ####################窗口管理####################结束
        #
        #
        ####################工具栏####################开始
        tool = QMenu('&工具栏', self)
        tool.setStatusTip('基本工具')
        viewMenu.addMenu(tool)

        calculator = QAction(QIcon('./QIcon/calculator.jpg'), '&计算器', self)
        calculator.setShortcut('C')
        calculator.setStatusTip('计算器')
        tool.addAction(calculator)
        calculator.triggered.connect(self.calculator_Win)

        ####################工具栏####################结束

        fullScreen = QAction('&全屏幕', self)
        fullScreen.setStatusTip('全屏')
        fullScreen.setShortcut('Shift+Alt+Enter')
        viewMenu.addAction(fullScreen)
        # fullScreen.triggered.connect(self.)

        propertyWindow = QAction('&属性窗口', self)
        propertyWindow.setStatusTip('属性窗口')
        propertyWindow.setShortcut('F4')
        viewMenu.addAction(propertyWindow)
        # propertyWindow.triggered.connect(self.)

        # 分析
        navigateMenu = self.menubar.addMenu('&分析(N)')

        # 工具
        toolMenu = self.menubar.addMenu('&工具(T)')

        # 扩展
        extendMenu = self.menubar.addMenu('&扩展(X)')
        # extendMenu.addAction()
        # 窗口
        windowMenu = self.menubar.addMenu('&窗口(W)')
        # windowMenu.addAction()
        # 帮助
        helpMenu = self.menubar.addMenu('&帮助(H)')

        help = QAction('&查看帮助', self)
        help.setShortcut('Ctrl+F1')
        help.setStatusTip('查看帮助')
        helpMenu.addAction(help)

        # help.triggered.connect(self.)
        ####################菜单栏####################结束

        ####################工具栏####################开始
        # 工具

        self.fileToolbar = self.addToolBar('打开文件')
        self.fileToolbar.addAction(openFile)

        self.exitToolbar = self.addToolBar('退出')
        self.exitToolbar.addAction(exitAction)

        self.calculatorTooolbar = self.addToolBar('计算器')
        self.calculatorTooolbar.addAction(calculator)
        ####################工具栏####################结束


