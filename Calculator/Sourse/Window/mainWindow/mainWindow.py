# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: mainWindow.py
    @date: 2019/7/18
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/2/23
-----------------------------------
    @desc:

-----------------------------------
"""

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtWidgets import QMenu, QMainWindow, QWidget, QListWidget, QStackedWidget, QListWidgetItem, QHBoxLayout, \
    QSplitter, QFrame, QVBoxLayout, QGridLayout, QStatusBar, QMenuBar, QTextEdit, QPushButton, QLabel

from Calculator.Sourse.Window.childWindow.calculatorWindow.Calculatormainwindow import Calculatormainwindow
from Calculator.Sourse.Window.commomHelper.commomHelper_loadQss.commomHelper_Qss import CommonhelperQss
from Calculator.Sourse.Window.mainWindow.QAction.qAction import Action
from Calculator.Sourse.Window.mainWindow.const.mainWindow_const import Const
from Calculator.Sourse.Window.commomHelper.commomHelper_image_scale.ImageScale import ImageScale
from Calculator.Sourse.Window.mainWindow.RightFrame.RightFrame1 import RightForm1
from Calculator.Sourse.Window.mainWindow.RightFrame.RightFrame2 import RightForm2
from Calculator.Sourse.Window.mainWindow.RightFrame.RightFrame3 import RightForm3
from Calculator.Sourse.Window.mainWindow.RightFrame.RightFrame4 import RightForm4
from Calculator.Sourse.Window.mainWindow.RightFrame.RightFrame5 import RightForm5


class MainWindow(QMainWindow):
    """
    主窗口界面
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # 初始化
        self.init()
        # ui设计
        self.setup_ui()
        # 创建右键菜单
        self.create_context_menu()
        # 主框体设计
        self.set_main_form()
        # 加载qss样式
        self.set_stylesheet()

    def init(self):
        self.setGeometry(Const.WIN_X, Const.WIN_Y, Const.WIN_WIDTH, Const.WIN_HEIGHT)
        self.setObjectName('mainWindow')
        self.setWindowIcon(QIcon("./image/Logo/logo.png"))
        self.setWindowTitle('IFR智能公式识别系统')

        # 加载图片缩放公共类
        self.imageScale = ImageScale()

    def setup_ui(self):
        """
        创建状态栏、菜单栏、工具栏
        """

        # 状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('准备就绪', 5000)
        # self.statusBar().setStyleSheet('background-color:lightGray;')

        # 菜单栏
        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
        # self.menuBar().setStyleSheet('background-color:lightGray;')

        # 文件
        self.fileMenu = self.menubar.addMenu('&文件(F)')

        # 调用自定义action
        self.openPimax = Action.action_b_2(self, 'openPimax', '&打开图片文件', 'Ctrl+P', '打开图片文件')
        self.openPimax.setIcon(QIcon('./image/openQpixmap.jpg'))
        self.openText = Action.action_b_2(self, 'openText', '&打开文本文件', 'Ctrl+T', '打开文本文件')
        self.openText.setIcon(QIcon('./image/openText.ico'))
        self.openFile = Action.action_b_3(self, 'openFile', '打开文件', '打开文件', self.fileMenu)
        self.openFile.addAction(self.openPimax)
        self.openFile.addAction(self.openText)

        self.openPimax.triggered.connect(lambda: self.get_image())
        self.openText.triggered.connect(lambda: self.get_text())
        self.openRecentFile = Action.action_a_2(self, 'openRecentFile', '&最近打开的文件', 'Ctrl+O', '最近打开的文件', self.fileMenu)
        # self.openRecentFile.triggered.connect(self.)
        self.save = Action.action_a_2(self, 'save', '&保存分析结果', 'Ctrl+S', '保存数据分析结果', self.fileMenu)
        # self.save.triggered.connect(self.)
        self.saveAs = Action.action_a_2(self, 'saveAs', '&另保存分析结果', 'Ctrl+Shift+S', '另保存数据分析结果', self.fileMenu)
        # self.saveAs.triggered.connect(self.)
        self.printf = Action.action_a_2(self, 'printef', '&打印分析结果', 'Ctrl+P', '打印数据分析结果', self.fileMenu)
        # self.printf.triggered.connect(self.)
        self.exitAction = Action.action_a_1(self, 'exitAction', './image/mainWindowIcon/toolBarIcon/exit.png', '&退出',
                                            'Ctrl+Q', '退出应用程序',
                                            self.fileMenu)
        self.exitAction.triggered.connect(self.close)

        # 编辑
        self.exitMenu = self.menubar.addMenu('&编辑(E)')
        #
        # ####################查找与替换####################开始
        self.search = Action.action_b_2(self, 'search', '&快速查找', 'Ctrl+F', '快速查找')
        self.replace = Action.action_b_2(self, 'replace', '&快速替换', 'Ctrl+H', '快速替换')

        # 新增二级菜单
        self.searchAndReplaceMenu = Action.action_b_3(self, 'searchAndReplaceMenu', '查找与替换', '查找与替换', self.exitMenu)
        self.searchAndReplaceMenu.addAction(self.search)
        self.searchAndReplaceMenu.addAction(self.replace)

        # self.search.triggered.connect(self.)
        # self.replace.triggered.connect(self.)

        # ####################查找与替换####################结束

        self.cut = Action.action_a_2(self, 'cut', '&剪切', 'Ctrl+X', '剪切', self.exitMenu)
        # self.cut.triggered.connect(self.)
        self.copy = Action.action_a_2(self, 'copy', '&复制', 'Ctrl+C', '复制', self.exitMenu)
        # self.copy.triggered.connect(self.)
        self.paste = Action.action_a_2(self, 'paste', '&粘贴', 'Ctrl+V', '粘贴', self.exitMenu)
        # self.paste.triggered.connect(self.)
        self.delete = Action.action_a_2(self, 'delect', '&删除', 'Del', '删除', self.exitMenu)
        # self.delect.triggered.connect(self.)
        self.selectAll = Action.action_a_2(self, 'selectAll', '&全选', 'Ctrl+Alt', '全选', self.exitMenu)
        # self.selectAll.triggered.connect(self.)

        # 视图
        self.viewMenu = self.menubar.addMenu('&视图(V)')

        self.notice = Action.action_a_2(self, 'notice', '&通知', 'Ctrl+Alt+X', '信息通知提醒', self.viewMenu)
        # self.notice.triggered.connect(self.)

        # ####################窗口管理####################开始
        self.window = Action.action_b_3(self, 'window', '&窗口', '展示一些基本窗口', self.viewMenu)

        # ####################窗口管理####################结束
        #
        #
        #
        # ####################工具栏####################开始
        self.tool = Action.action_b_3(self, 'tool', '&工具栏', '基本工具', self.viewMenu)

        self.calculator = Action.action_a_1(self, 'calculator', './image/calculator.jpg', '&计算器',
                                            'C', '计算器', self.viewMenu)
        self.calculator.triggered.connect(lambda: self.calculator_win())

        # ####################工具####################结束
        self.fullScreen = Action.action_a_2(self, 'fullScreen', '&全屏幕', 'Shift+Alt+Enter', '全屏', self.viewMenu)
        # self.fullScreen.triggered.connect(self.)
        self.propertyWindow = Action.action_a_2(self, 'propertyWindow', '&属性窗口', 'F4', '属性窗口', self.viewMenu)
        # self.propertyWindow.triggered.connect(self.)
        #

        # 分析
        self.navigateMenu = self.menubar.addMenu('&分析(N)')
        #

        # 工具
        self.toolMenu = self.menubar.addMenu('&工具(T)')
        #

        # 扩展
        self.extendMenu = self.menubar.addMenu('&扩展(X)')
        #

        # 窗口
        self.windowMenu = self.menubar.addMenu('&窗口(W)')
        #

        # 帮助
        self.helpMenu = self.menubar.addMenu('&帮助(H)')

        self.help = Action.action_a_2(self, 'help ', '&查看帮助', 'Ctrl+F1', '查看帮助', self.helpMenu)
        # self.help.triggered.connect(self.)
        # ####################菜单####################结束

        ################################################################################################################

        # ####################工具栏####################开始
        # 工具

        self.pixmapToolbar = self.addToolBar('打开图形文件')
        self.textToolbar = self.addToolBar('打开文本文件')
        self.pixmapToolbar.addAction(self.openPimax)
        self.textToolbar.addAction(self.openText)

        self.exitToolbar = self.addToolBar('退出')
        self.exitToolbar.addAction(self.exitAction)

        self.calculatorTooolbar = self.addToolBar('计算器')
        self.calculatorTooolbar.addAction(self.calculator)

        # ####################工具栏####################结束

        #  槽函数线程

    # 创建右键菜单
    def create_context_menu(self):
        """
        创建右键菜单
        :return:
        """
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        # 创建QMenu
        self.contextMenu = QMenu(self)

        # ####################工具栏管理####################开始
        self.toolBarManagementMenu = Action.action_b_4(self, 'toolBarManagementMenu', '&工具栏管理', self.contextMenu)
        # 未完成
        # ####################工具栏管理####################结束

        self.minAtion = Action.action_a_1(self, 'minAction', './image/min.png', '&最小化', 'Ctrl+M', '最小化窗口',
                                          self.contextMenu)

        self.contextMenu.addSeparator()  # 添加分隔线

        self.cutAction = Action.action_a_2(self, 'cutAction', '&剪切', 'Ctrl+X', '剪切', self.contextMenu)
        self.copyAction = Action.action_a_2(self, 'copyAction', '&复制', 'Ctrl+C', '复制', self.contextMenu)
        self.pasteAction = Action.action_a_2(self, 'pasteAction', '&粘贴', 'Ctrl+V', '粘贴', self.contextMenu)
        self.deleteAction = Action.action_a_2(self, 'delectAction', '&删除', 'Del', '删除', self.contextMenu)
        self.selectAllAction = Action.action_a_2(self, 'selectAllAction', '&全选', 'Ctrl+Alt', '全选', self.contextMenu)

        self.contextMenu.addSeparator()  # 添加分隔线

        self.closeAction = Action.action_a_1(self, 'closeAction', './image/Exit.png', '&退出', 'Ctrl+W', '退出',
                                             self.contextMenu)

        self.minAtion.triggered.connect(self.show_mininized_window)

        self.closeAction.triggered.connect(self.quit_window)
        # self.selectAllAction.triggered.connect(self.)
        # self.cutAction.triggered.connect(self.)
        # self.copyAction.triggered.connect(self.)
        # self.pasteAction.triggered.connect(self.)
        # self.delectAction.triggered.connect(self.)

    # ****************************** 业务逻辑 *********************************
    def set_stylesheet(self):
        """
         加载Qss样式表
        :return:
        """
        style_file = './Window/mainWindow/Qss/mainWindow.qss'
        qss_style = CommonhelperQss.read_qss(style_file)
        self.setStyleSheet(qss_style)

    def set_action_connect(self):
        """
        菜单栏、工具栏槽函数连接
        :return:
        """
        pass

    def calculator_win(self):
        """
        加载计算器窗口
        :return:
        """
        self.calculator_Win = Calculatormainwindow()
        self.calculator_Win.show()

    def set_main_form(self):
        """
        窗体布局以及主框体设计
        :return:
        """
        # 主框体
        self.mainSpiltter = QSplitter(Qt.Vertical)
        self.mainSpiltter.setObjectName('mainSpiltter')

        self.mainSpiltterLayout = QVBoxLayout()

        # 设置主窗口中心窗体
        self.setCentralWidget(self.mainSpiltter)

        # *******工作区间*******
        self.workWidget = QSplitter()
        self.workWidget.setObjectName('workWidget')
        self.mainSpiltter.addWidget(self.workWidget)

        self.workWidgetLayout = QHBoxLayout()
        self.workWidget.setLayout(self.workWidgetLayout)

        self.leftWidget = QFrame()
        self.leftWidget.setObjectName('leftWidget')
        self.leftWidget.setFrameShape(QFrame.StyledPanel)
        self.leftWidget.setMaximumWidth(230)

        self.leftWidgetLayout = QVBoxLayout()
        self.leftWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.leftWidget.setLayout(self.leftWidgetLayout)

        # self.hideBtn = QLabel()
        # self.hideBtn.setObjectName('hideBtn')
        # self.hideBtn.setPixmap(QPixmap('./image/mainWindowIcon/showAndHideIcon/hide0.ico'))
        #
        # self.showBtn = QLabel()
        # self.showBtn.setObjectName('showBtn')
        # self.showBtn.setPixmap(QPixmap('./image/mainWindowIcon/showAndHideIcon/show0.ico'))

        # 存放按钮
        self.widget = QWidget()
        self.widget.setObjectName('widget')
        self.leftWidgetLayout.addWidget(self.widget)

        pixmap = self.imageScale.pixmap_scale('./image/Logo/logo0.png', 204, 80)

        self.logoIamgeLabel = QLabel(self.widget)
        self.logoIamgeLabel.setObjectName('logoImageLabel')
        self.logoIamgeLabel.setPixmap(pixmap)

        self.widgetLayout = QGridLayout()
        self.widget.setLayout(self.widgetLayout)

        self.widgetLayout.addWidget(self.logoIamgeLabel, 0, 1)

        # 多界面
        # QListWidget + QStackedWidget实现
        self.leftListWidget = QListWidget()  # 左侧选项列表
        self.leftListWidget.setObjectName('leftListWidget')
        self.rightWidget = QStackedWidget()  # 右侧框体
        self.rightWidget.setObjectName('rightWidget')

        self.leftWidgetLayout.addWidget(self.leftListWidget)

        self.workWidgetLayout.addWidget(self.leftWidget)
        self.workWidgetLayout.addWidget(self.rightWidget)

        # ********左侧选项列表布局以及设置******************************
        # 设置左侧选项列表大小
        self.leftListWidget.setMinimumWidth(Const.LEFTWIDGET_WIDTH)
        # 左侧选项列表与右侧框体的index对应绑定
        self.leftListWidget.currentRowChanged.connect(self.rightWidget.setCurrentIndex)
        # 去掉边框
        self.leftListWidget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.leftListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.leftListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        list_str = ['智能识别', '公式生成器', '学习资源区', '设置', '关于']

        # 左侧选项添加
        for i in range(5):
            self.item = QListWidgetItem(list_str[i], self.leftListWidget)
            self.item.setSizeHint(QSize(Const.ITEM_WIDTH, Const.ITEM_HEIGHT))
            # 居中显示
            self.item.setTextAlignment(Qt.AlignCenter)

        # 设置默认选中item[1]
        self.leftListWidget.setCurrentRow(0)

        # ********右侧主框体布局以及设置**********************************
        self.rightForm1 = RightForm1()
        self.rightForm2 = RightForm2()
        self.rightForm3 = RightForm3()
        self.rightForm4 = RightForm4()
        self.rightForm5 = RightForm5()
        self.rightWidget.addWidget(self.rightForm1)
        self.rightWidget.addWidget(self.rightForm2)
        self.rightWidget.addWidget(self.rightForm3)
        self.rightWidget.addWidget(self.rightForm4)
        self.rightWidget.addWidget(self.rightForm5)

        # #############################################################
        # 消息通知框
        self.messageInform = MesageFrame()
        self.messageInform.setObjectName('messageInform')
        # 消息通知框默认隐藏
        self.messageInform.hide()

        self.mainSpiltter.addWidget(self.messageInform)

        # *****侧边栏*****
        # 右侧边栏
        self.rightBar = QFrame()
        self.rightBar.setObjectName('rightBar')
        self.rightBar.setFixedWidth(35)
        self.rightBar.setFrameShape(QFrame.StyledPanel)

        self.rightBarLayout = QVBoxLayout()
        self.rightBar.setLayout(self.rightBarLayout)

        self.workWidgetLayout.addWidget(self.rightBar)

        # 右侧边栏控件

        # 右侧边栏添加控件

        # 下侧边栏
        self.bottomBar = QFrame()
        self.bottomBar.setObjectName('bottomBar')
        self.bottomBar.setMaximumHeight(35)
        self.bottomBar.setFrameShape(QFrame.StyledPanel)

        self.bottomBarLayout = QHBoxLayout()
        self.bottomBarLayout.setAlignment(Qt.AlignRight)  # 右对齐
        self.bottomBar.setLayout(self.bottomBarLayout)

        self.mainSpiltter.addWidget(self.bottomBar)

        # 下侧边栏控件
        # 留白控件
        blank = QLabel(self.bottomBar)
        blank.setObjectName('blank')

        self.informText = QLabel(self.bottomBar)
        self.informText.setObjectName('informText')
        self.informText.setText('通知')

        self.informBtn = QPushButton(self.bottomBar)
        self.informBtn.setObjectName('informBtn')
        self.informBtn.resize(QSize(35, 35))
        self.informBtn.setIcon(QIcon('./image/mainWindowIcon/messageBarBtnIcon/inform0.png'))
        self.informBtn.clicked.connect(lambda: self.open_inform_frame())

        # 下侧边栏添加控件

        self.bottomBarLayout.addWidget(self.informBtn)
        self.bottomBarLayout.addWidget(self.informText)
        self.bottomBarLayout.addWidget(blank)

    # ****************************业务逻辑******************************
    # 右键菜单
    def show_context_menu(self):
        """
        右键点击时调用的函数
        :return:
        """
        # 显示菜单前，将它移动到鼠标点击的位置
        self.contextMenu.exec_(QCursor.pos())

    # 最小化窗口
    def show_mininized_window(self):
        """
        :return:
        """
        self.showMinimized()

    # 最大化窗口
    def show_maximized_window(self):
        """

        :return:
        """
        self.showMaximized()

    # 复原窗口
    def show_restore_window(self):
        """

        :return:
        """
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # 关闭窗口
    def quit_window(self):
        """

        :return:
        """
        self.close()

    # 打开文件
    def get_image(self):

        """
            getOpenFileName():返回用户所选择文件的名称，并打开该文件
            第一个参数用于指定父组件
            第二个参数指定对话框标题
            第三个参数指定目录
            第四个参数是文件扩展名过滤器
        """
        pass
        # fname, _ = QFileDialog.getOpenFileName(self, '选择图形文件', 'C:\\', "*.jpg *.gif *.png")
        # self.pixmapLabel.setPixmap(QPixmap(fname))

    def get_text(self):
        """

        :return:
        """
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

    def open_inform_frame(self):
        self.messageInform.show()


class MesageFrame(QSplitter):
    """
    消息通知框
    用来显示历史消息以及通知
    """

    def __init__(self):
        super(MesageFrame, self).__init__()
        self.init()
        self.setup_ui()
        self.set_form_layout()

    def init(self):
        self.setWindowFlags(Qt.FramelessWindowHint)

    def setup_ui(self):
        # 侧边栏
        self.topBar = QFrame()
        self.topBar.setObjectName('barFrame')
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFixedHeight(35)

        self.leftBar = QFrame()
        self.leftBar.setObjectName('barFrame')
        self.leftBar.setFrameShape(QFrame.StyledPanel)
        self.leftBar.setFixedWidth(35)

        self.rightBar = QFrame()
        self.rightBar.setObjectName('barFrame')
        self.rightBar.setFrameShape(QFrame.StyledPanel)
        self.rightBar.setFixedWidth(35)

        # 消息显示框
        self.messageEdit = QTextEdit()
        self.messageEdit.setObjectName('messageEdit')

        # 按钮
        self.settingBtn = QPushButton(self.topBar)
        self.settingBtn.setObjectName('resultFrameSettingBtn')
        self.settingBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm1Image/setting.png'))
        self.settingBtn.setMaximumWidth(30)
        self.minBtn = QPushButton(self.topBar)
        self.minBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm1Image/min.png'))
        self.minBtn.setMaximumWidth(30)
        self.minBtn.clicked.connect(lambda: self.hide_message_frame())

    def set_form_layout(self):
        """

        :return:
        """
        all_layout = QHBoxLayout()
        all_layout.setSpacing(0)
        self.setLayout(all_layout)

        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.topBar)
        splitter.addWidget(self.messageEdit)

        all_layout.addWidget(self.leftBar)
        all_layout.addWidget(splitter)
        all_layout.addWidget(self.rightBar)

        top_bar_layout = QHBoxLayout()
        self.topBar.setLayout(top_bar_layout)

        top_bar_layout.setAlignment(Qt.AlignRight)
        top_bar_layout.addWidget(self.settingBtn)
        top_bar_layout.addWidget(self.minBtn)

    def hide_message_frame(self):
        self.hide()
