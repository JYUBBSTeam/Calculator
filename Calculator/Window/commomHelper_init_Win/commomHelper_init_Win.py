'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：创建一个自定义标题栏的公共类
    类：CommonHelper_titleBar:自定义标题栏的公共类

'''

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap, QCursor

TITLE_BAR_HEIGHT = 40
TITLE_BUTTON_SIZE = 40
TITLE_ICON_MAG = 40
TITLE_MIN_ICON = './QIcon/min.png'
TITLE_RESTORE_ICON = './QIcon/restore.png'
TITLE_CLOSE_ICON = './QIcon/exit.png'


class CommonHelper_titleBar(QWidget):
    '''
            功能：  1.关闭，最小化，复原三个按钮的基本功能
                    2.双击标题栏窗口最大化或者缩小
                    3.鼠标点击拖动窗口
                    4.显示标题和图标
    '''
    def __init__(self):
        super(CommonHelper_titleBar, self).__init__()

        self.InitializeWindow()

    def InitializeWindow(self):
        self.isPressed = False
        self.setFixedHeight(TITLE_BAR_HEIGHT)
        self.InitializeViews()


    def InitializeViews(self):
        # 标题图标标签
        self.iconLabel = QLabel(self)
        # 标题标签
        self.titleLabel = QLabel(self)
        # 最小化按钮
        self.minButton = QPushButton(self)
        # 复原按钮
        self.restoreButton = QPushButton(self)
        # 关闭按钮
        self.closeButton = QPushButton(self)
        # 设置大小
        self.minButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE)
        self.restoreButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE)
        self.closeButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE)

        self.iconLabel.setAlignment(Qt.AlignLeft)
        self.titleLabel.setAlignment(Qt.AlignLeft)

        self.minButton.setIcon(QIcon(TITLE_MIN_ICON))
        self.restoreButton.setIcon(QIcon(TITLE_RESTORE_ICON))
        self.closeButton.setIcon(QIcon(TITLE_CLOSE_ICON))

        self.minButton.clicked.connect(self.ShowMininizedWindow)
        self.restoreButton.clicked.connect(self.ShowRestoreWindow)
        self.closeButton.clicked.connect(self.CloseWindow)

        # 水平布局
        self.lay = QHBoxLayout(self)
        self.setLayout(self.lay)

        self.lay.setSpacing(0)  # 去除控件之间的距离
        self.lay.setContentsMargins(0, 0, 0, 0)

        # 往布局里添加控件
        self.lay.addWidget(self.iconLabel)
        self.lay.addWidget(self.titleLabel)
        self.lay.addWidget(self.minButton)
        self.lay.addWidget(self.restoreButton)
        self.lay.addWidget(self.closeButton)

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
    def CloseWindow(self):
        self.close()

    def SetTitle(self, str):
        self.titleLabel.setText(str)

    def SetIcon(self, pix):
        self.iconLabel.setPixmap(pix.scaled(self.iconLabel.size() - QSize(TITLE_ICON_MAG, TITLE_ICON_MAG)))

    ################################
    #        重写鼠标事件           #
    ################################
    # # 鼠标双击事件
    def mouseDoubleClickEvent(self, event):
        self.ShowRestoreWindow()
        return QWidget().mouseDoubleClickEvent(event)

    # 鼠标单击事件
    def mousePressEvent(self, event):
        self.isPressed = True
        self.starPos = event.globalPos()
        return QWidget().mousePressEvent(event)

    # 事件触发
    def mouseReleaseEvent(self, event):
        self.isPressed = False
        return QWidget().mouseReleaseEvent(event)

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.isPressed:
            if self.isMaximized():
                self.showNormal()

            # 计算窗口应该移动的距离
            movePos = event.globalPos()
            self.starPos = event.globalPos()
            self.move(self.pos() + movePos)

        return QWidget().mouseMoveEvent(event)
