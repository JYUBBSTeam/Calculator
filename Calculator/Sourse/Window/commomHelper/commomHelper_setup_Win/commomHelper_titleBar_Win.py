# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
    @创建人：Liang
    @创建时间：2019/7/18
    @最后一次编辑时间：
    @描述：创建一个自定义标题栏的功能帮助类
    @类：CommonHelper_titleBar:自定义标题栏的功能帮助类
    @函数：
"""

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QCursor
from Calculator.Sourse.Window.commomHelper.const.commom_helper_titlebar_win_const import Const
from Calculator.Sourse.Window.commomHelper.commomHelper_loadQss.commomHelper_Qss import CommonhelperQss


# 自定义标题栏公共类
class CommonhelperTitlebar(QWidget):
    """
    功能：  1.关闭，最小化，复原三个按钮的基本功能
            2.双击标题栏窗口最大化或者缩小
            3.鼠标点击拖动窗口
            4.显示标题和图标
    """

    def __init__(self):
        super(CommonhelperTitlebar, self).__init__()

        # # 加载qss样式表
        # style_file = './Window/commomHelper/commomHelper_setup_Win/Qss/titleBar.qss'
        # qss_style = CommonhelperQss.read_qss(style_file)
        # self.setStyleSheet(qss_style)

        self.initialize_window()

    def initialize_window(self):
        """

        :return:
        """
        self.isPressed = False
        self.setFixedHeight(Const.TITLE_BAR_HEIGHT)
        self.initialize_views()

    def initialize_views(self):
        """
        初始化
        :return:
        """
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
        # 最大化按钮
        self.maxButton = QPushButton(self)
        self.maxButton.setObjectName("maxButton")
        # 关闭按钮
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('closeButton')
        # 设置大小
        self.minButton.setFixedSize(Const.TITLE_BUTTON_SIZE, Const.TITLE_BUTTON_SIZE)
        self.restoreButton.setFixedSize(Const.TITLE_BUTTON_SIZE, Const.TITLE_BUTTON_SIZE)
        self.maxButton.setFixedSize(Const.TITLE_BUTTON_SIZE, Const.TITLE_BUTTON_SIZE)
        self.closeButton.setFixedSize(Const.TITLE_BUTTON_SIZE, Const.TITLE_BUTTON_SIZE)

        self.iconLabel.setAlignment(Qt.AlignLeft)
        self.titleLabel.setAlignment(Qt.AlignLeft)

        # 设置图标
        self.minButton.setIcon(QIcon(Const.TITLE_MIN_ICON))
        self.restoreButton.setIcon(QIcon(Const.TITLE_RESTORE_ICON))
        self.closeButton.setIcon(QIcon(Const.TITLE_CLOSE_ICON))

        # 设置提示信息
        self.iconLabel.setToolTip('标题图标')
        self.minButton.setToolTip('最小化')
        self.restoreButton.setToolTip('复原')
        self.closeButton.setToolTip('关闭')

        # 设置鼠标手势
        self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.restoreButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))

        # 水平布局
        self.lay = QHBoxLayout(self)
        self.lay.setObjectName('lay')
        self.setLayout(self.lay)

        self.lay.setSpacing(Const.SPACING)  # 去除控件之间的距离
        self.lay.setContentsMargins(Const.MARGINS, Const.MARGINS, Const.MARGINS, Const.MARGINS)

        # 往布局里添加控件
        self.lay.addWidget(self.iconLabel)
        self.lay.addWidget(self.titleLabel)
        self.lay.addWidget(self.minButton)
        self.lay.addWidget(self.restoreButton)
        self.lay.addWidget(self.maxButton)
        self.lay.addWidget(self.closeButton)
