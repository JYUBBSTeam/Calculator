'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：计算器窗口界面
    类：
'''
import sys
import math

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QCursor, QPainterPath, QPainter, QColor, QBrush

from Calculator.Window.childWindow.calculatorWindow.calculator_setup_UI import setupUI
from Calculator.Window.childWindow.calculatorWindow.calculator_init_UI import init_UI
from Calculator.Window.commomHelper_init_Win.commomHelper_init_Win import CommonHelper_titleBar   # 加载自定义标题栏的类
from Calculator.Window.commomHelper_loadQss.commomHelper_Qss import CommonHelper_qss

PADDING = 4     # 设置边界宽度为4
sys.setrecursionlimit(10000)


class calculator_Window(QWidget):
    '''
        计算器界面窗口
    '''
    def __init__(self,  parent = None):
        super(calculator_Window, self).__init__(parent)
        # 加载Qss样式表
        styleFile = './childWindow/calculatorWindow/Qss/calculatorWindow.qss'
        qssStyle = CommonHelper_qss.readQss(styleFile)
        self.setStyleSheet(qssStyle)

        # 布局
        AllLayout = QVBoxLayout()
        AllLayout.setSpacing(0)
        AllLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(AllLayout)

        self.title = CommonHelper_titleBar()

        self.centerWidget = QWidget()
        AllLayout.addWidget(self.title)
        AllLayout.addWidget(self.centerWidget)

        self.initUi = calculator_Window.init_Ui(self.centerWidget)
        self.setupUi = calculator_Window.setup_Ui(self.centerWidget)

        ####################窗体无边框初始化####################开始
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)  # 设置无边框
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 将form设置为透明
        self.SHADOW_WIDTH = 0  # 边框距离
        self.isLeftPressDown = False  # 鼠标左键是否按下
        self.dragPosition = 0  # 拖动时坐标
        self.Numbers = self.enum(UP=0, DOWN=1, LEFT=2, RIGHT=3, LEFTTOP=4, LEFTBOTTOM=5, RIGHTBOTTOM=6, RIGHTTOP=7,
                                 NONE=8)  # 枚举参数
        self.setMinimumHeight(750)  # 窗体最小高度
        self.setMinimumWidth(700)  # 窗体最小宽度
        self.dir = self.Numbers.NONE  # 初始化鼠标状态 : 默认
        self.setMouseTracking(True)

    # 枚举参数
    def enum(self, **enums):
        return type('Enum', (), enums)

    def region(self, cursorGlobalpoint):
        '''
            获取窗体在屏幕上的位置区域，tl为topleft点，rb为rightbottom点
        '''
        rect = self.rect()
        tl = self.mapToGlobal(rect.topLeft())
        rb = self.mapToGlobal(rect.bottomRight())

        x = cursorGlobalpoint.x()
        y = cursorGlobalpoint.y()

        if (tl.x() + PADDING >= x and tl.x() <= x and tl.y() + PADDING >= y and tl.y() <= y):
            # 左上角
            self.dir = self.Numbers.LEFTTOP
            self.setCursor(QCursor(Qt.SizeFDiagCursor))  # 设置鼠标形状
        elif (x >= rb.x() - PADDING and x <= rb.x() and y >= rb.y() - PADDING and y <= rb.y()):
            # 右下角
            self.dir = self.Numbers.RIGHTBOTTOM
            self.setCursor(QCursor(Qt.SizeFDiagCursor))
        elif (x <= tl.x() + PADDING and x >= tl.x()):
            # 左下角
            self.dir = self.Numbers.LEFTBOTTOM
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        elif (x <= rb.x() and x >= rb.x() - PADDING and y >= tl.y() and y <= tl.y() and y <= tl.y() + PADDING):
            # 右上角
            self.dir = self.Numbers.RIGHTTOP
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        elif (x <= tl.x() + PADDING and x >= tl.x()):
            # 左边
            self.dir = self.Numbers.LEFT
            self.setCursor(QCursor(Qt.SizeHorCursor))
        elif (x <= rb.x() and x >= rb.x() - PADDING):
            # 右边
            self.dir = self.Numbers.RIGHT
            self.setCursor(QCursor(Qt.SizeHorCursor))
        elif (y >= tl.y() and y <= tl.y() + PADDING):
            # 上边
            self.dir = self.Numbers.UP
            self.setCursor(QCursor(Qt.SizeVerCursor))
        elif (y <= rb.y() and y >= rb.y() - PADDING):
            # 下边
            self.dir = self.Numbers.DOWN
            self.setCursor(QCursor(Qt.SizeVerCursor))
        else:
            # 默认
            self.dir = self.Numbers.NONE
            self.setCursor(QCursor(Qt.PointingHandCursor))

    #######################################
    ###########重置鼠标点击事件#############
    #
    def mouseReleaseEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.isLeftPressDown = False
            if (self.dir != self.Numbers.NONE):
                self.releaseMouse()
                self.setCursor(QCursor(Qt.ArrowCursor))

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.isLeftPressDown = True
            if (self.dir != self.Numbers.NONE):
                self.mouseGrabber()
            else:
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        gloPoint = event.globalPos()
        rect = self.rect()
        tl = self.mapToGlobal(rect.topLeft())
        rb = self.mapToGlobal(rect.bottomRight())

        if (not self.isLeftPressDown):
            self.region(gloPoint)
        else:
            if (self.dir != self.Numbers.NONE):
                rmove = QRect(tl, rb)
                if (self.dir == self.Numbers.LEFT):
                    if (rb.x() - gloPoint.x() <= self.minimumWidth()):
                        rmove.setX(tl.x())
                    else:
                        rmove.setX(gloPoint.x())
                elif (self.dir == self.Numbers.RIGHT):
                    # print(u"is change")
                    rmove.setWidth(gloPoint.x() - tl.x())
                elif (self.dir == self.Numbers.UP):
                    if (rb.y() - gloPoint.y() <= self.minimumHeight()):
                        rmove.setY(tl.y())
                    else:
                        rmove.setY(gloPoint.y())
                elif (self.dir == self.Numbers.DOWN):
                    rmove.setHeight(gloPoint.y() - tl.y())
                elif (self.dir == self.Numbers.LEFTTOP):
                    if (rb.x() - gloPoint.x() <= self.minimumWidth()):
                        rmove.setX(tl.x())
                    else:
                        rmove.setX(gloPoint.x())
                    if (rb.y() - gloPoint.y() <= self.minimumHeight()):
                        rmove.setY(tl.y())
                    else:
                        rmove.setY(gloPoint.y())
                elif (self.dir == self.Numbers.RIGHTTOP):
                    rmove.setWidth(gloPoint.x() - tl.x())
                    rmove.setY(gloPoint.y())
                elif (self.dir == self.Numbers.LEFTBOTTOM):
                    rmove.setX(gloPoint.x())
                    rmove.setHeight(gloPoint.y() - tl.y())
                elif (self.dir == self.Numbers.RIGHTBOTTOM):
                    rmove.setWidth(gloPoint.x() - tl.x())
                    rmove.setHeight(gloPoint.y() - tl.y())
                else:
                    pass

                self.setGeometry(rmove)

            else:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
    def paintEvent(self, event):
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRect(10, 10, self.width() - 20, self.height() - 20)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.fillPath(path, QBrush(Qt.white))
        color = QColor(0, 0, 0, 50)
        for i in range(0, 10):
            path = QPainterPath()
            path.setFillRule(Qt.WindingFill)
            path.addRect(10 - i, 10 - i, self.width() - (10 - i) * 2, self.height() - (10 - i) * 2)
            color.setAlpha(150 - math.sqrt(i) * 50)
            painter.setPen(color)
            painter.drawPath(path)


    ####################窗体无边框初始化####################结束

    def setup_Ui(self):
        self.setup_Win = setupUI.setup_Window(self)

    def init_Ui(self):
        self.init_Ui = init_UI.init_Ui(self)









