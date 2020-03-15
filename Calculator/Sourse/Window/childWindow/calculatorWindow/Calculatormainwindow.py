# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
    Project -> File  : Calculator -> calculatorMainWindow
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：计算器窗口主界面
    类：calculatorMainWindow
    函数：
"""
import sys
import math

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QToolTip, QMessageBox, QTabWidget
from PyQt5.QtCore import Qt, QSize, QPoint, QThread, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QPainterPath, QPainter, QColor, QBrush, QPixmap, QIcon, QFont

from Calculator.Sourse.Window.childWindow.calculatorWindow.UIdesigne.baseConversion import Uiconversionofnumbersystems
from Calculator.Sourse.Window.commomHelper.commomHelper_setup_Win.commomHelper_titleBar_Win import \
    CommonhelperTitlebar  # 加载自定义标题栏的类
# from Calculator.Sourse.Window.commomHelper.commomHelper_loadQss.commomHelper_Qss import CommonhelperQss
from Calculator.Sourse.Window.childWindow.calculatorWindow.UIdesigne.Standardcalculator import Standardcalculator
from Calculator.Sourse.Window.childWindow.calculatorWindow.UIdesigne.Sciencecalculator import Sciencecalculator
# 加载定义的常量
from Calculator.Sourse.Window.childWindow.calculatorWindow.const.calculatorMainWindow_const import Const


class Calculatormainwindow(QWidget):
    """
        计算器主界面窗口
    """
    _startPos = None
    _endPos = None
    _isTracking = None

    def __init__(self):
        super(Calculatormainwindow, self).__init__()
        self.fla = True
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)  # 设置无边框
        self.setAttribute(Qt.WA_TranslucentBackground, self.fla)  # 将form设置为透明
        self.setMinimumHeight(Const.MINIMUMHEIGHT)  # 设置窗体最小高度
        self.setMinimumWidth(Const.MINIMUMWIDTH)  # 设置窗体最小宽度

        # 布局
        all_layout = QVBoxLayout()
        all_layout.setObjectName('all_layout')
        all_layout.setSpacing(Const.SET_SPACING)
        self.setLayout(all_layout)

        # 调整布局与边界距离
        all_layout.setContentsMargins(Const.SET_CONTENTSMARGINS, Const.SET_CONTENTSMARGINS, Const.SET_CONTENTSMARGINS,
                                      Const.SET_CONTENTSMARGINS)

        # 调用自定义标题栏
        self.title = CommonhelperTitlebar()
        self.title.setObjectName('title')

        self.title.spinnerBtn = QPushButton(self.title)  # 创建下拉列表按钮
        self.title.spinnerBtn.setObjectName("spinnerBtn")
        self.title.spinnerBtn.resize(40, 40)
        self.title.spinnerBtn.setIcon(QIcon(Const.SPINNERBTN_ICON))
        self.title.spinnerBtn.setStyleSheet("background-color:white;")
        self.title.spinnerBtn.move(60, 0)
        QToolTip.setFont(QFont("sansSerif", 10))
        self.title.spinnerBtn.setToolTip("功能列表")
        self.title.spinnerBtn.clicked.connect(self.spinner_btn_pressed)

        # 自定义最小化、关闭按钮槽函数连接
        self.title.minButton.clicked.connect(self.show_mininized_window)
        self.title.closeButton.clicked.connect(self.close_window)

        # 隐藏复原和最大化按钮(不可用）
        self.title.restoreButton.setHidden(self.fla)
        self.title.maxButton.setHidden(self.fla)

        # 自定义标题Icon和内容
        title_icon = QPixmap("./image/calculator.jpg")
        self.title.iconLabel.setPixmap(title_icon.scaled(40, 40))
        self.title.titleLabel.setText('标准计算器')
        self.title.titleLabel.setFont(QFont("STSong", 16))  # 华文宋体
        self.title.titleLabel.resize(40, 40)

        # 界面主窗口
        self.centerWidget = QTabWidget()
        self.centerWidget.setObjectName('centerWidget')

        all_layout.addWidget(self.title)
        all_layout.addWidget(self.centerWidget)

        self.setWindowTitle('计算器')
        self.setWindowIcon(QIcon("./image/calculator.jpg"))

        # 下拉列表
        self.spinner()
        # 加载窗口
        self.show_win()

    # ************************** 业务逻辑 *************************
    def show_win(self):
        """
        显示默认窗口你（高级计算器窗口）
        :return:
        """
        self.standardCalculator = Standardcalculator()
        self.scienceCalculator = Sciencecalculator()
        self.baseConversionWindow = Uiconversionofnumbersystems()
        self.centerWidget.addTab(self.standardCalculator, "标准计算器")
        self.centerWidget.addTab(self.scienceCalculator, "科学计算器")
        self.centerWidget.addTab(self.baseConversionWindow, "程序员计算器")

    def paintEvent(self, event):
        """
        重写paintEvent，实现边框阴影
        :param event:
        :return:
        """
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRect(10, 10, self.width() - 20, self.height() - 20)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, self.fla)
        painter.fillPath(path, QBrush(Qt.white))
        color = QColor(0, 0, 0, 50)
        for i in range(0, 10):
            path = QPainterPath()
            path.setFillRule(Qt.WindingFill)
            path.addRect(10 - i, 10 - i, self.width() - (10 - i) * 2, self.height() - (10 - i) * 2)
            color.setAlpha(150 - math.sqrt(i) * 50)
            painter.setPen(color)
            painter.drawPath(path)

    # #########################自定义下拉列表 #######################开始
    # 自定义下拉列表，实现几种计算界面之间的切换
    def spinner(self):
        """
        表自定义下拉列表
        :return:
        """
        # 创建下拉列表框
        self.spinnerQwidget = QWidget(self)
        self.spinnerQwidget.setObjectName('spinnerQwidget')
        self.spinnerQwidget.setGeometry(70, 50, 250, 250)
        self.spinnerQwidget.setStyleSheet('background-color:white;')
        self.spinnerQwidget.hide()

        self.spinnerLayout = QVBoxLayout(self.spinnerQwidget)
        self.spinnerLayout.setObjectName("spinnerLayout")

        # 标准计算器切换按钮
        self.StandardCalculatorBtn = QPushButton("标准计算器")
        self.StandardCalculatorBtn.setObjectName("calculatorBtn")
        self.StandardCalculatorBtn.clicked.connect(lambda: self.calculator_win_change(1))
        # 科学计算器切换按钮
        self.scienceCalculatorBtn = QPushButton("科学计算器")
        self.scienceCalculatorBtn.setObjectName("scienceCalculatorBtn")
        self.scienceCalculatorBtn.clicked.connect(lambda: self.calculator_win_change(2))
        # 程序员计算器切换按钮
        self.baseConversionBtn = QPushButton("程序员计算器")
        self.baseConversionBtn.setObjectName("baseConversionBtn")
        self.baseConversionBtn.clicked.connect(lambda: self.calculator_win_change(3))

        self.StandardCalculatorBtn.setStyleSheet("background-color:gray;")
        self.baseConversionBtn.setStyleSheet("background-color:gray;")
        self.spinnerQuitBtn = QPushButton(self.spinnerQwidget)
        self.spinnerQuitBtn.setObjectName("spinnerQuitBtn")
        self.spinnerQuitBtn.setIcon(QIcon("./image/spinnerQuit.png"))
        self.spinnerQuitBtn.setStyleSheet("background-color:cyan;")
        self.spinnerQuitBtn.clicked.connect(lambda: self.spinner_btn_pressed())

        # 分隔控件的空白窗口
        self.separator = QWidget(self.spinnerQwidget)
        self.separator.setObjectName("separator")
        self.separator.resize(150, 20)

        # 往下拉列表框添加控件
        self.spinnerLayout.addWidget(self.StandardCalculatorBtn)
        self.spinnerLayout.addWidget(self.scienceCalculatorBtn)
        self.spinnerLayout.addWidget(self.baseConversionBtn)
        self.spinnerLayout.addWidget(self.separator)
        self.spinnerLayout.addWidget(self.spinnerQuitBtn)

    # #########################自定义下拉列表 #######################结束

    # ***************************** 业务逻辑 ********************************

    # ####################设置窗口大小槽函数####################开始
    def show_mininized_window(self):
        """
        最小化窗口
        :return:
        """
        self.showMinimized()

    # # 最大化窗口
    # def show_maximized_window(self):
    #     '''
    #
    #     :return:
    #     '''
    #     self.showMaximized()

    # # 复原窗口
    # def show_restore_window(self):
    #     '''
    #
    #     :return:
    #     '''
    #     if self.isMaximized():
    #         self.showNormal()
    #     else:
    #         self.showMaximized()

    def close_window(self):
        """
        关闭窗口
        :return:
        """
        self.close()

    def set_title(self, _str):
        """
        设置状态信息
        :param _str:
        :return:
        """
        self.titleLabel.set_text(_str)

    def set_icon(self, pix):
        """
        设置icon
        :param pix:
        :return:
        """
        self.iconLabel.setPixmap(pix.scaled(self.iconLabel.size() - QSize(Const.TITLE_ICON_MAG, Const.TITLE_ICON_MAG)))

    # ####################设置窗口大小槽函数####################结束

    # #########################calculator窗口切换#######################开始

    def calculator_win_change(self, flag):
        """
        窗口切换
        :param flag:
        :return:
        """
        self.flag = flag
        if self.flag == 1:
            if self.centerWidget.currentIndex() == self.flag - 1:
                QMessageBox.information(self.centerWidget, "提示", "已经为当前窗口！", QMessageBox.Ok)
            else:
                self.centerWidget.setCurrentIndex(self.flag - 1)
                self.title.titleLabel.setText('标准计算器')
        elif self.flag == 2:
            if self.centerWidget.currentIndex() == self.flag - 1:
                QMessageBox.information(self.centerWidget, "提示", "已经为当前窗口！", QMessageBox.Ok)
            else:
                self.centerWidget.setCurrentIndex(self.flag - 1)
                self.title.titleLabel.setText('科学计算器')
        elif self.flag == 3:
            if self.centerWidget.currentIndex() == self.flag - 1:
                QMessageBox.information(self.centerWidget, "提示", "已经为当前窗口！", QMessageBox.Ok)
            else:
                self.centerWidget.setCurrentIndex(self.flag - 1)
                self.title.titleLabel.setText('程序员计算器')

    # #########################calculator窗口切换#######################结束

    # #########################实现窗口拖动#######################开始
    # 重写鼠标事件
    def mousePressEvent(self, e: QMouseEvent):
        """
        鼠标点击事件
        :param e:
        :return:
        """
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._starPos = QPoint(e.x(), e.y())

    def mouseMoveEvent(self, e: QMouseEvent):
        """
        鼠标移动事件
        :param e:
        :return:
        """
        self._endPos = e.pos() - self._starPos
        self.move(self.pos() + self._endPos)

    def mouseReleaseEvent(self, e: QMouseEvent):
        """
        鼠标释放事件
        :param e:
        :return:
        """
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._starPos = None
            self._endPos = None

    # #########################实现窗口拖动#######################结束

    def spinner_btn_pressed(self):
        """
        下拉列表槽函数
        :return:
        """
        if self.spinnerQwidget.isHidden():
            self.spinnerQwidget.show()
        else:
            self.spinnerQwidget.hide()

    def spinner_quit_btn_pressed(self):
        """
        隐藏下拉列表按钮槽函数
        :return:
        """
        self.spinnerQwidget.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculatormainwindow()
    win.show()

    sys.exit(app.exec_())
