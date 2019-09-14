'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：创建一个自定义标题栏的功能帮助类
    类：CommonHelper_titleBar:自定义标题栏的功能帮助类
    函数：
'''

import const    # 导入常量模块
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from Calculator.Calculator.Sourse.Window.commomHelper.commomHelper_loadQss.commomHelper_Qss import CommonHelper_qss

const.TITLE_BAR_HEIGHT = 40
const.TITLE_BUTTON_SIZE = 40
const.TITLE_MIN_ICON = './image/min.png'
const.TITLE_RESTORE_ICON = './image/restore.png'
const.TITLE_CLOSE_ICON = './image/exit.png'
const.SPACING = 0
const.MARGINS = 0


# 自定义标题栏公共类
class CommonHelper_titleBar(QWidget):
    '''
            功能：  1.关闭，最小化，复原三个按钮的基本功能
                    2.双击标题栏窗口最大化或者缩小
                    3.鼠标点击拖动窗口
                    4.显示标题和图标
    '''
    def __init__(self):
        super(CommonHelper_titleBar, self).__init__()

        # 加载qss样式表
        styleFile = './Window/commomHelper/commomHelper_setup_Win/Qss/titleBar.qss'
        qssStyle = CommonHelper_qss.readQss(styleFile)
        self.setStyleSheet(qssStyle)

        self.InitializeWindow()

    def InitializeWindow(self):
        self.isPressed = False
        self.setFixedHeight(const.TITLE_BAR_HEIGHT)
        self.InitializeViews()


    def InitializeViews(self):
        # 标题图标标签
        self.iconLabel = QLabel(self)
        self.iconLabel.setObjectName('iconLabel')
        # 标题标签
        self.titleLabel = QLabel(self)
        self.titleLabel.setObjectName('titleLabel')
        # 最小化按钮
        self.minButton = QPushButton(self)
        self.setObjectName('minButton')
        # 复原按钮
        self.restoreButton = QPushButton(self)
        self.restoreButton.setObjectName('restoreButton')
        # 关闭按钮
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        # 设置大小
        self.minButton.setFixedSize(const.TITLE_BUTTON_SIZE, const.TITLE_BUTTON_SIZE)
        self.restoreButton.setFixedSize(const.TITLE_BUTTON_SIZE, const.TITLE_BUTTON_SIZE)
        self.closeButton.setFixedSize(const.TITLE_BUTTON_SIZE, const.TITLE_BUTTON_SIZE)

        self.iconLabel.setAlignment(Qt.AlignLeft)
        self.titleLabel.setAlignment(Qt.AlignLeft)

        self.minButton.setIcon(QIcon(const.TITLE_MIN_ICON))
        self.restoreButton.setIcon(QIcon(const.TITLE_RESTORE_ICON))
        self.closeButton.setIcon(QIcon(const.TITLE_CLOSE_ICON))

        # 水平布局
        self.lay = QHBoxLayout(self)
        self.lay.setObjectName('lay')
        self.setLayout(self.lay)

        self.lay.setSpacing(const.SPACING)  # 去除控件之间的距离
        self.lay.setContentsMargins(const.MARGINS, const.MARGINS, const.MARGINS, const.MARGINS)

        # 往布局里添加控件
        self.lay.addWidget(self.iconLabel)
        self.lay.addWidget(self.titleLabel)
        self.lay.addWidget(self.minButton)
        self.lay.addWidget(self.restoreButton)
        self.lay.addWidget(self.closeButton)

