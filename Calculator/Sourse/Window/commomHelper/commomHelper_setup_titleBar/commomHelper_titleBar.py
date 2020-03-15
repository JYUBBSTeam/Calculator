# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: main.py
    @date: 2019/7/18
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/2/23
-----------------------------------
    @desc:
        创建一个自定义标题栏公共类
-----------------------------------
"""

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QCursor
from Calculator.Sourse.Window.commomHelper.const.commom_helper_titlebar_win_const import Const
from Calculator.Sourse.Window.commomHelper.commomHelper_loadQss.commomHelper_Qss import CommonhelperQss


# 自定义标题栏公共类
class CommonhelperTitleBar(QWidget):
    """
    功能：
        1.关闭，最小化，最大化，复原按钮的基本功能
        2.显示标题和图标
    """

    def __init__(self):
        super(CommonhelperTitleBar, self).__init__()

        self.initialize_window()
        self.load_qss()

    def initialize_window(self):
        """

        :return:
        """
        self.setObjectName('titleBar')

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
        self.minButton.setObjectName('titleBarButton')
        self.minButton.setIconSize(QSize(30, 30))

        # 复原按钮
        self.restoreButton = QPushButton(self)
        self.restoreButton.setObjectName('titleBarButton')
        self.restoreButton.setIconSize(QSize(Const.ICON_WIDTH, Const.ICON_HEIGHT))
        # 最大化按钮
        self.maxButton = QPushButton(self)
        self.maxButton.setObjectName("titleBarButton")
        self.maxButton.setIconSize(QSize(Const.ICON_WIDTH, Const.ICON_HEIGHT))
        # 关闭按钮
        self.closeButton = QPushButton(self)
        self.closeButton.setObjectName('titleBarButton')
        self.closeButton.setIconSize(QSize(Const.ICON_WIDTH, Const.ICON_HEIGHT))
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
        self.allLayout = QHBoxLayout(self)
        self.allLayout.setObjectName('allLayout')
        self.setLayout(self.allLayout)

        self.allLayout.setSpacing(Const.SPACING)  # 去除控件之间的距离
        self.allLayout.setContentsMargins(Const.MARGINS, Const.MARGINS, Const.MARGINS, Const.MARGINS)

        # 往布局里添加控件
        self.allLayout.addWidget(self.iconLabel)
        self.allLayout.addWidget(self.titleLabel)
        self.allLayout.addWidget(self.minButton)
        self.allLayout.addWidget(self.restoreButton)
        self.allLayout.addWidget(self.maxButton)
        self.allLayout.addWidget(self.closeButton)

    def load_qss(self):
        style_file = './Window/commomHelper/Qss/commomHelper_titleBar.qss'
        qss_style = CommonhelperQss.read_qss(style_file)
        self.setStyleSheet(qss_style)
