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

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QFrame, QPushButton, QTabWidget, QHBoxLayout, QGridLayout, \
    QTextEdit, QVBoxLayout, QColorDialog, QGroupBox, QLabel, QRadioButton, QProgressBar
from PyQt5.QtCore import Qt, QSize

from Calculator.Sourse.Window.mainWindow.RightFrame.EquationEditor import EquationEditor
from Calculator.Sourse.Window.mainWindow.RightFrame.WritingPad import WritingPad


class WritingPadWidget(QWidget):
    def __init__(self):
        super(WritingPadWidget, self).__init__()

        self.init()
        self.setup_ui()
        self.set_form_layout()

    def init(self):
        self.penColor = Qt.black
        self.penSize = 2

    def setup_ui(self):
        # 结果框
        self.resultFrame = QFrame(self)
        self.resultFrame.setObjectName('resultFrame')
        self.textEdit = QTextEdit()
        self.textEdit.setObjectName('textEdit')

        self.frame1 = QFrame()
        self.frame1.setObjectName('frame1')

        # 手写台
        self.writingPad = WritingPad(self.penColor, self.penSize)
        self.writingPad.setObjectName('writingPad')
        self.writingPad.setFrameShape(QFrame.StyledPanel)

        self.frame2 = QFrame()
        self.frame2.setObjectName('frame2')

        # 控制面板
        self.controlPanel = QFrame(self)
        self.controlPanel.setObjectName('controlPanel')

        # 笔触样式预览
        self.viewBox = QGroupBox()
        self.viewBox.setObjectName('viewBox')

        self.viewLabel = QLabel()
        self.viewLabel.setObjectName('viewLabel')

        # 加载控制面板控件
        self.control_panel()
        # 加载控制面板布局
        self.set_controlpanel_layout()

    def control_panel(self):
        """
        控制面板控件
        :return:
        """
        self.buttonWidget = QWidget()

        self.radioButton1 = QRadioButton('经典笔触颜色样式')
        self.radioButton1.setObjectName('radioButton')
        self.radioButton2 = QRadioButton('自定义笔触颜色样式 ')
        self.radioButton2.setObjectName('radioButton')

        # 按钮控件
        self.resumeBtn = QPushButton(self.buttonWidget)
        self.resumeBtn.setObjectName('paintBtn')
        self.resumeBtn.setIconSize(QSize(50, 50))
        self.resumeBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm2Image/writingPad/resume.png'))
        self.resumeBtn.clicked.connect(lambda: self.resume())

        self.cancelBtn = QPushButton(self.buttonWidget)
        self.cancelBtn.setObjectName('paintBtn')
        self.cancelBtn.setIconSize(QSize(50, 50))
        self.cancelBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm2Image/writingPad/cancel.png'))
        self.cancelBtn.clicked.connect(lambda: self.cancel())

        self.clearBtn = QPushButton(self.buttonWidget)
        self.clearBtn.setObjectName('paintBtn')
        self.clearBtn.setIconSize(QSize(50, 50))
        self.clearBtn.setIcon(QIcon('./image/mainWindowIcon/RightForm2Image/writingPad/clear.jpg'))
        self.clearBtn.clicked.connect(lambda: self.clear())

        # 笔触颜色样式
        self.colorForm1 = QLabel()
        self.colorForm1.setObjectName('colorLabel1')
        self.colorForm2 = QLabel()
        self.colorForm2.setObjectName('colorLabel2')
        self.colorForm3 = QLabel()
        self.colorForm3.setObjectName('colorLabel3')
        self.colorForm4 = QLabel()
        self.colorForm4.setObjectName('colorLabel4')
        self.colorForm5 = QLabel()
        self.colorForm5.setObjectName('colorLabel5')
        self.colorForm6 = QLabel()
        self.colorForm6.setObjectName('colorLabel6')
        self.colorForm7 = QLabel()
        self.colorForm7.setObjectName('colorLabel7')

        # 调色板
        self.colorControlPad = QPushButton()
        self.colorControlPad.setObjectName('colorToolBtn')
        self.colorControlPad.setText('打开调色板')
        self.colorControlPad.clicked.connect(lambda: self.q_color_dialog())
        # 用于显示调色板选定的样式
        self.colorControlPadForm = QLabel()
        self.colorControlPadForm.setObjectName('colorStyle')
        self.colorControlPadForm.setStyleSheet('background-color:white')

        # 笔触大小
        self.label = QLabel('笔触样式大小')
        self.label.setObjectName('label')

        self.progressBar = QProgressBar()
        self.progressBar.setObjectName('progressBar')

        self.sizeLabel = QLabel('20')
        self.sizeLabel.setObjectName('label')

    def set_controlpanel_layout(self):
        self.controlPanelLayout = QVBoxLayout()
        self.controlPanel.setLayout(self.controlPanelLayout)

        self.controlPanelLayout.addWidget(self.buttonWidget, 1)
        self.controlPanelLayout.addWidget(self.viewBox, 1)

        # buttonWidget
        self.buttonWidgetLayout = QGridLayout()
        self.buttonWidget.setLayout(self.buttonWidgetLayout)

        self.buttonWidgetLayout.addWidget(self.resumeBtn, 0, 0)
        self.buttonWidgetLayout.addWidget(self.cancelBtn, 0, 1)
        self.buttonWidgetLayout.addWidget(self.clearBtn, 0, 2)

        self.buttonWidgetLayout.addWidget(self.radioButton1, 1, 0, 1, 4)
        self.buttonWidgetLayout.addWidget(self.colorForm1, 2, 0)
        self.buttonWidgetLayout.addWidget(self.colorForm2, 2, 1)
        self.buttonWidgetLayout.addWidget(self.colorForm3, 2, 2)
        self.buttonWidgetLayout.addWidget(self.colorForm4, 2, 3)
        self.buttonWidgetLayout.addWidget(self.colorForm5, 2, 4)
        self.buttonWidgetLayout.addWidget(self.colorForm6, 2, 5)
        self.buttonWidgetLayout.addWidget(self.colorForm7, 2, 6)

        self.buttonWidgetLayout.addWidget(self.radioButton2, 3, 0, 1, 4)
        self.buttonWidgetLayout.addWidget(self.colorControlPad, 4, 0, 1, 2)
        self.buttonWidgetLayout.addWidget(self.colorControlPadForm, 4, 2)

        self.buttonWidgetLayout.addWidget(self.label, 5, 0, 1, 3)
        self.buttonWidgetLayout.addWidget(self.progressBar, 6, 0, 1, 6)
        self.buttonWidgetLayout.addWidget(self.sizeLabel, 6, 6)

        self.viewBoxLayout = QHBoxLayout()
        self.viewBox.setLayout(self.viewBoxLayout)
        self.viewBoxLayout.addWidget(self.viewLabel)

    def set_form_layout(self):
        self.allLayout = QVBoxLayout()
        self.setLayout(self.allLayout)

        self.writinglayout = QHBoxLayout()
        self.frame1.setLayout(self.writinglayout)

        self.allLayout.addWidget(self.resultFrame, 1)
        self.allLayout.addWidget(self.frame1, 2)

        self.writinglayout.addWidget(self.writingPad, 7)
        self.writinglayout.addWidget(self.controlPanel, 2)

        self.resultFrameLayout = QHBoxLayout()
        self.resultFrame.setLayout(self.resultFrameLayout)
        self.resultFrameLayout.addWidget(self.textEdit)

    # ***********************业务逻辑*******************************
    def resume(self):
        pass

    def cancel(self):
        pass

    def clear(self):
        self.writingPad.clear()

    def set_color(self):
        pass

    def q_color_dialog(self):
        color = QColorDialog.getColor()
        self.penColor = color.name()
        self.colorControlPadForm.setStyleSheet('background-color:' + self.penColor)


class RightForm2(QWidget):
    def __init__(self):
        super(RightForm2, self).__init__()
        self.setup_ui()
        self.init()
        self.set_form_layout()

    def setup_ui(self):
        # 选项卡面板
        self.tabWidget = QTabWidget()
        self.tabWidget.setObjectName('tabWidget')

        self.widget1 = WritingPadWidget()
        self.widget2 = EquationEditor()

    def init(self):
        pass

    def set_form_layout(self):
        # 总布局
        self.allLayout = QHBoxLayout()
        self.setLayout(self.allLayout)

        self.allLayout.addWidget(self.tabWidget)

        self.tabWidget.addTab(self.widget1, '手写台')
        self.tabWidget.addTab(self.widget2, '公式编辑器')

    # ***********************业务逻辑************************
