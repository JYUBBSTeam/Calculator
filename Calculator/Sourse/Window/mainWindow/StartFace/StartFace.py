# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: StartFace.py
    @date: 2020/2/26
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/2/26
-----------------------------------
    @desc:
        启动界面
        参考于GitHub项目（https://github.com/PyQt5/PyQt/tree/master/QPropertyAnimation）
        思路：
            先根据窗口大小随机创建一些点
            遍历这些点找到跟它自己关联的点
            动画开始画圆点、画连线
            动画改变这些点的透明度, 用到了属性动画QPropertyAnimation
----------------------------------- 
"""
from random import random
from time import time
import time as Time

from PyQt5.QtCore import QPropertyAnimation, QObject, pyqtProperty, QEasingCurve, \
    Qt, QRectF, pyqtSignal, QRect
from PyQt5.QtGui import QColor, QPainterPath, QPainter, QPalette, QBrush, QPixmap, QPen, QPaintEvent
from PyQt5.QtWidgets import QWidget, qApp, QSplashScreen, QDesktopWidget
from Calculator.Sourse.Window.mainWindow.const.initSplash_const import Const

try:
    from Lib import pointtool  # @UnusedImport @UnresolvedImport

    getDistance = pointtool.getDistance
    findClose = pointtool.findClose
except:
    import math


    def get_distance(p1, p2):
        return math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2)


    def find_close(points):
        plen = len(points)
        for i in range(plen):
            closest = [None, None, None, None, None]
            p1 = points[i]
            for j in range(plen):
                p2 = points[j]
                dte1 = get_distance(p1, p2)
                if p1 != p2:
                    placed = False
                    for k in range(5):
                        if not placed:
                            if not closest[k]:
                                closest[k] = p2
                                placed = True
                    for k in range(5):
                        if not placed:
                            if dte1 < get_distance(p1, closest[k]):
                                closest[k] = p2
                                placed = True
            p1.closest = closest


class Target:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(QObject):
    valueChanged = pyqtSignal()

    def __init__(self, x, ox, y, oy, *args, **kwargs):
        super(Point, self).__init__(*args, **kwargs)
        self.__x = x
        self._x = x
        self.originX = ox
        self._y = y
        self.__y = y
        self.originY = oy
        # 5个闭合点
        self.closest = [0, 0, 0, 0, 0]
        # 圆半径
        self.radius = 2 + random() * 2
        # 连线颜色
        self.lineColor = QColor(156, 217, 249)
        # 圆颜色
        self.circleColor = QColor(156, 217, 249)

    def init_animation(self):
        # 属性动画
        if not hasattr(self, 'xanimation'):
            self.xanimation = QPropertyAnimation(
                self, b'x', self, valueChanged=self.valueChanged.emit,
                easingCurve=QEasingCurve.InOutSine)
            self.yanimation = QPropertyAnimation(
                self, b'y', self, valueChanged=self.valueChanged.emit,
                easingCurve=QEasingCurve.InOutSine,
                finished=self.update_animation)
            self.update_animation()

    def update_animation(self):
        self.xanimation.stop()
        self.yanimation.stop()
        duration = (1 + random()) * 1000
        self.xanimation.setDuration(duration)
        self.yanimation.setDuration(duration)
        self.xanimation.setStartValue(self.__x)
        self.xanimation.setEndValue(self.originX - 50 + random() * 100)
        self.yanimation.setStartValue(self.__y)
        self.yanimation.setEndValue(self.originY - 50 + random() * 100)
        self.xanimation.start()
        self.yanimation.start()

    @pyqtProperty(float)
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @pyqtProperty(float)
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y


class SplashScreen(QSplashScreen):
    """
    启动界面
    """

    def __init__(self, *args, **kwargs):
        super(SplashScreen, self).__init__(*args, **kwargs)
        self.setObjectName('SplashScreen')
        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.resize(900, 600)

        # 设置启动窗口居中
        screen = QDesktopWidget()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

        self.text = "初始化程序...0%"
        self.points = []
        self.target = Target(self.width() / 2, self.height() / 2)
        self.init_points()

    # *************************业务逻辑*****************************
    def paintEvent(self, event):
        super(SplashScreen, self).paintEvent(event)
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # painter.fillRect(self.rect(), Qt.black)

        self.animate(painter)
        painter.end()

    def mouseMoveEvent(self, event):
        super(SplashScreen, self).mouseMoveEvent(event)
        # 鼠标移动时更新xy坐标
        self.target.x = event.x()
        self.target.y = event.y()
        self.update()

    def init_points(self):
        t = time()
        self.points.clear()
        # 创建点
        step_x = self.width() / 20
        step_y = self.height() / 20
        for x in range(0, self.width(), int(step_x)):
            for y in range(0, self.height(), int(step_y)):
                ox = x + random() * step_x
                oy = y + random() * step_y
                point = Point(ox, ox, oy, oy)
                point.valueChanged.connect(self.update)
                self.points.append(point)
        print(time() - t)

        t = time()
        # 每个点寻找5个闭合点
        find_close(self.points)
        print(time() - t)

    def animate(self, painter):
        for p in self.points:
            # 检测点的范围
            value = abs(get_distance(self.target, p))
            if value < 4000:
                # 其实就是修改颜色透明度
                p.lineColor.setAlphaF(0.3)
                p.circleColor.setAlphaF(0.6)
            elif value < 20000:
                p.lineColor.setAlphaF(0.1)
                p.circleColor.setAlphaF(0.3)
            elif value < 40000:
                p.lineColor.setAlphaF(0.02)
                p.circleColor.setAlphaF(0.1)
            else:
                p.lineColor.setAlphaF(0)
                p.circleColor.setAlphaF(0)

            # 画线条
            if p.lineColor.alpha():
                for pc in p.closest:
                    if not pc:
                        continue
                    path = QPainterPath()
                    path.moveTo(p.x, p.y)
                    path.lineTo(pc.x, pc.y)
                    painter.save()
                    painter.setPen(p.lineColor)
                    painter.drawPath(path)
                    painter.restore()

            # 画圆
            painter.save()
            painter.setPen(Qt.NoPen)
            painter.setBrush(p.circleColor)
            painter.drawRoundedRect(QRectF(
                p.x - p.radius, p.y - p.radius, 2 * p.radius, 2 * p.radius), p.radius, p.radius)
            painter.restore()

            # 开启动画
            p.init_animation()


# 测试
if __name__ == '__main__':
    import sys
    import cgitb

    sys.excepthook = cgitb.enable(1, None, 5, '')
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    qApp.processEvents()

    # splash.close()  # 隐藏启动界面
    sys.exit(app.exec_())
