# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: RightFrame1.py
    @date: 2020/2/26
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/2/26
-----------------------------------
    @desc:
    
----------------------------------- 
"""
import PIL.ExifTags
from PIL import Image

from PyQt5.QtWidgets import QWidget, QDockWidget, QGroupBox, QGraphicsView, QHBoxLayout, QVBoxLayout, QGridLayout, \
    QTextEdit, QListWidget, QListWidgetItem, QScrollArea, QPushButton, QTabWidget, QFileDialog, QGraphicsScene, \
    QGraphicsPixmapItem, QFrame, QSplitter

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QDragEnterEvent, QDragMoveEvent, QDragLeaveEvent, QDropEvent, QCursor, QPixmap


class RightForm1(QFrame):
    """
    右侧框体1
    """

    def __init__(self):
        super(RightForm1, self).__init__()
        self.init()
        self.setup_ui()
        self.set_form_layout()

    def init(self):
        pass

    def setup_ui(self):
        # ***************左侧******************
        self.loadingFrame = QFrame()
        self.loadingFrame.setObjectName('loadingFrame')
        self.loadingFrame.setFrameShape(QFrame.StyledPanel)
        # 最小化以及设置按钮管理栏
        self.loadingFrameBar = QWidget(self.loadingFrame)
        self.loadingFrameBar.setObjectName('loadingFrameBar')
        self.loadingFrameBar.resize(self.loadingFrame.width(), 20)

        self.loadingFrameSettingBtn = QPushButton(self.loadingFrameBar)
        self.loadingFrameSettingBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm1Image/setting.png'))
        self.loadingFrameSettingBtn.setMaximumWidth(30)
        self.loadingFrameMinBtn = QPushButton(self.loadingFrameBar)
        self.loadingFrameMinBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm1Image/min.png'))
        self.loadingFrameMinBtn.setMaximumWidth(30)
        self.loadingFrameMinBtn.clicked.connect(lambda: self.hide_loadframe())

        # 选项卡面板
        self.loadingTab = QTabWidget(self.loadingFrame)
        self.loadingTab.setObjectName('loadingTab')

        # *********图片加载模式UI设计**********
        self.imageLoadingForm = QWidget(self.loadingTab)
        self.imageLoadingForm.setObjectName('imageLoadingForm')

        self.form1_a = QWidget(self.imageLoadingForm)
        self.form1_a.setObjectName('form1_a')

        self.groupBox1 = QGroupBox(self.form1_a)
        self.groupBox1.setObjectName('groupBox1')
        self.groupBox1.setTitle('图片显示：')

        self.graphicsView = QGraphicsView(self.groupBox1)
        self.graphicsView.setObjectName('graphicsView')

        # 显示图片信息框
        self.textEdit1 = QTextEdit(self.form1_a)
        self.textEdit1.setObjectName('textEdit1')
        self.textEdit1.setReadOnly(True)
        self.textEdit1.setText('当前还没加载图片，' + '\n' + '无法查看图片信息!!!')

        self.form2_a = QWidget(self.imageLoadingForm)
        self.form2_a.setObjectName('form2_a')

        self.groupBox2 = QGroupBox(self.form2_a)
        self.groupBox2.setObjectName('groupBox2')
        self.groupBox2.setTitle('图片列表')

        # 加载图片列表
        self.imageListWidget = QListWidget(self.form2_a)
        self.imageListWidget.setObjectName('imageListWidget')
        self.imageListWidget.setToolTip('图片加载列表')
        self.imageListWidget.setMinimumWidth(600)

        self.buttonWidget = QWidget()
        self.buttonWidget.setObjectName('buttonWidget')

        self.imageOpenBtn = QPushButton('打开图片')
        self.imageOpenBtn.setObjectName('imageOpenBtn')

        self.imageOpenBtn.clicked.connect(lambda: self.load_image())

        # 图片选择改变事件监听
        self.imageListWidget.currentRowChanged.connect(lambda: self.image_selecttion_change(
            self.imageListWidget.currentItem().text()))
        self.imageListWidget.currentItemChanged.connect(lambda: self.display_image_message(self.imageListWidget.
                                                                                           currentItem().text()))

        # 工具栏
        self.imageToolFrame = QFrame(self.form2_a)
        self.imageToolFrame.setObjectName('imageToolFrame')
        self.imageToolFrame.setFrameShape(QFrame.StyledPanel)

        # 开始识别按钮
        self.startIdentifyBtn = QPushButton('开始识别')
        self.startIdentifyBtn.setObjectName('startIdentifyBtn')

        # ######################################################

        # **********文档加载模式UI设计***********
        self.textLoadingForm = QWidget(self.loadingFrame)
        # self.textLoadingForm.setObjectName('textLoadingForm')
        #
        # self.form1_b = QWidget(self.textLoadingForm)
        # self.form1_b.setObjectName('form1_b')
        # # 显示文档信息框
        # self.textEdit2 = QTextEdit(self.form1_b)
        # self.textEdit2.setObjectName('textEdit2')
        #
        # # 工具栏
        # self.toolWidget2 = QWidget()
        # self.toolWidget2.setObjectName('toolWidget2')
        # self.textOpenBtn = QPushButton('打开文档')
        # self.textOpenBtn.setObjectName('textOpenBtn')

        # ############################################################################
        #
        # ***************右侧******************
        self.resultFrame = QFrame()
        self.resultFrame.setObjectName('resultFrame')
        self.resultFrame.setFrameShape(QFrame.StyledPanel)
        # 最小化以及设置按钮管理栏
        self.resultFrameBar = QWidget()
        self.resultFrameBar.setObjectName('resultFrameBar')
        self.resultFrameBar.resize(self.resultFrame.width(), 20)

        self.resultFrameSettingBtn = QPushButton(self.loadingFrameBar)
        self.resultFrameSettingBtn.setObjectName('resultFrameSettingBtn')
        self.resultFrameSettingBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm1Image/setting.png'))
        self.resultFrameSettingBtn.setMaximumWidth(30)
        self.resultFrameMinBtn = QPushButton(self.loadingFrameBar)
        self.resultFrameMinBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm1Image/min.png'))
        self.resultFrameMinBtn.setMaximumWidth(30)
        self.resultFrameMinBtn.clicked.connect(lambda: self.hide_resultframe())

        self.resultEdit = QTextEdit()
        self.resultEdit.setObjectName('resultEdit')

        # ###########################################################################
        # 分隔符部件
        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.setObjectName('mainSplitter')

    def set_form_layout(self):
        # 主框体总布局
        self.allLayout = QHBoxLayout()
        self.setLayout(self.allLayout)
        self.allLayout.addWidget(self.mainSplitter)

        self.mainSplitter.addWidget(self.loadingFrame)
        self.mainSplitter.addWidget(self.resultFrame)

        # 左侧布局
        self.loadingFrameLayout = QGridLayout()
        self.loadingFrame.setLayout(self.loadingFrameLayout)
        self.loadingFrameLayout.addWidget(self.loadingFrameBar, 0, 0)
        self.loadingFrameLayout.addWidget(self.loadingTab, 1, 0)

        # ******************加载图片模式********************
        self.imageLoadingFormLayout = QGridLayout()
        self.imageLoadingForm.setLayout(self.imageLoadingFormLayout)

        self.imageLoadingFormLayout.addWidget(self.form1_a, 0, 0, 3, 1)
        self.imageLoadingFormLayout.addWidget(self.form2_a, 3, 0, 2, 1)

        self.loadingFrameBarLayout = QHBoxLayout()
        self.loadingFrameBar.setLayout(self.loadingFrameBarLayout)
        self.loadingFrameBarLayout.setAlignment(Qt.AlignRight)
        self.loadingFrameBarLayout.addWidget(self.loadingFrameSettingBtn)
        self.loadingFrameBarLayout.addWidget(self.loadingFrameMinBtn)

        self.form1Layout = QHBoxLayout()
        self.form1_a.setLayout(self.form1Layout)
        self.form1Layout.addWidget(self.groupBox1, 3)
        self.form1Layout.addWidget(self.textEdit1, 1)

        self.qHBoxLayout = QHBoxLayout()
        self.groupBox1.setLayout(self.qHBoxLayout)
        self.qHBoxLayout.addWidget(self.graphicsView)

        self.form2Layout = QGridLayout()
        self.form2_a.setLayout(self.form2Layout)
        self.form2Layout.addWidget(self.groupBox2, 0, 0, 1, 3)
        self.form2Layout.addWidget(self.imageToolFrame, 0, 4)

        self.groupBox2Layout = QHBoxLayout()
        self.groupBox2.setLayout(self.groupBox2Layout)
        self.groupBox2Layout.addWidget(self.imageListWidget)
        self.groupBox2Layout.addWidget(self.buttonWidget)

        self.buttonWidgetLayout = QGridLayout()
        self.buttonWidget.setLayout(self.buttonWidgetLayout)
        self.buttonWidgetLayout.addWidget(self.imageOpenBtn)

        self.imageToolFrameLayout = QVBoxLayout()
        self.imageToolFrame.setLayout(self.imageToolFrameLayout)
        self.imageToolFrameLayout.addWidget(self.startIdentifyBtn)
        # ******************加载文档模式********************

        self.loadingTab.addTab(self.imageLoadingForm, '图片加载智能识别 ')
        self.loadingTab.addTab(self.textLoadingForm, '文档加载智能识别')

        # 右侧布局
        self.resultFrameBarLayout = QHBoxLayout()
        self.resultFrameBar.setLayout(self.resultFrameBarLayout)

        self.resultFrameBarLayout.setAlignment(Qt.AlignRight)
        self.resultFrameBarLayout.addWidget(self.resultFrameSettingBtn)
        self.resultFrameBarLayout.addWidget(self.resultFrameMinBtn)

        self.resultFrameLayout = QGridLayout()
        self.resultFrame.setLayout(self.resultFrameLayout)
        self.resultFrameLayout.addWidget(self.resultFrameBar)
        self.resultFrameLayout.addWidget(self.resultEdit)

    # ******************************业务逻辑**********************************

    def load_image(self):
        """
        将图片加载到图片列表
        :return:
        """
        image_path, image_type = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        # 增加图片目录
        self.imageListWidget.addItem(image_path)
        # 显示图片
        self.display_image(image_path)
        # self.display_image_message(image_path)

    def display_image(self, image_path):
        """
        显示图片
        :param image_path:
        :return:
        """
        self.image_path = image_path
        self.image = QPixmap()
        self.image.load(self.image_path)
        self.graphicsView.scene = QGraphicsScene()
        item = QGraphicsPixmapItem(self.image)
        self.graphicsView.scene.addItem(item)
        self.graphicsView.setScene(self.graphicsView.scene)

    def image_selecttion_change(self, current_path):
        self.current_path = current_path

        self.display_image(self.current_path)
        # self.display_image_message(self.current_path)

    def display_image_message(self, image_path):
        message = ''
        self.image_path = image_path

        message = self.load_image_message(self.image_path)

        self.textEdit1.setText(message)

    def load_image_message(self, image_path):
        """
        会返回一个字典，包含图像的各种属性信息
        :param image_path:
        :return:
        """
        self.image_path = image_path
        message = ''
        image = Image.open(self.image_path)

        # 还没有完成**************
        return message

    def load_text(self):
        pass

    def hide_loadframe(self):
        self.loadingFrame.hide()

    def hide_resultframe(self):
        self.resultFrame.hide()
