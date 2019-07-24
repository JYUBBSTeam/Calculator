'''
    创建人：Liang
    创建时间：2019/7/21
    最后一次编辑时间：
    描述：窗口设置
    类：setupUI:窗口设置
'''

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QCursor

PADDING = 4


class setupUI():
    '''

    '''
    def setup_Window(self):
        '''
            无边框窗口实现移动和缩放功能，并设置窗口阴影
        '''
        ####################实现窗口设置####################开始
        #
        #   重写Qt窗口事件
        #
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)  # 设置无边框
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        #self.setAttribute(Qt.WA_TranslucentBackground, True)  # 透明

        self.SHADOW_WIDTH = 0  # 边框距离
        self.isLeftPressDown = False  # 鼠标左键是否按下
        self.dragPosition = 0  # 拖动时坐标
        self.Numbers = setupUI.enum(self, UP=0, DOWN=1, LEFT=2, RIGHT=3, LEFTTOP=4, LEFTBOTTOM=5, RIGHTBOTTOM=6, RIGHTTOP=7,
                                 NONE=8)  # 枚举参数
        self.setMinimumHeight(700)  # 窗体最小高度
        self.setMinimumWidth(600)  # 窗体最小宽度
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


    ####################实现窗口设置####################结束


