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
        self.minButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE)
        self.restoreButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE)
        self.closeButton.setFixedSize(TITLE_BUTTON_SIZE, TITLE_BUTTON_SIZE)

        self.iconLabel.setAlignment(Qt.AlignLeft)
        self.titleLabel.setAlignment(Qt.AlignLeft)

        self.minButton.setIcon(QIcon(TITLE_MIN_ICON))
        self.restoreButton.setIcon(QIcon(TITLE_RESTORE_ICON))
        self.closeButton.setIcon(QIcon(TITLE_CLOSE_ICON))

        # 水平布局
        self.lay = QHBoxLayout(self)
        self.lay.setObjectName('lay')
        self.setLayout(self.lay)

        self.lay.setSpacing(0)  # 去除控件之间的距离
        self.lay.setContentsMargins(0, 0, 0, 0)

        # 往布局里添加控件
        self.lay.addWidget(self.iconLabel)
        self.lay.addWidget(self.titleLabel)
        self.lay.addWidget(self.minButton)
        self.lay.addWidget(self.restoreButton)
        self.lay.addWidget(self.closeButton)

