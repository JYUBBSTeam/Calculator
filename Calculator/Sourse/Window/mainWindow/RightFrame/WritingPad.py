# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: WritingPad.py
    @date: 2020/3/22
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/3/22
-----------------------------------
    @desc:
    
----------------------------------- 
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPainter, QMouseEvent
from PyQt5.QtWidgets import QFrame


class WritingPad(QFrame):
    """
    手写台
    """

    def __init__(self, pen_color, pen_size):
        super(WritingPad, self).__init__()

        self.penColor = pen_color
        self.penSize = pen_size

        self.init()

    def init(self):
        # 只有按下鼠标才会跟踪事件
        self.setMouseTracking(False)
        # 一个列表用于保存点
        self.pos_xy = []

    # ***********************业务逻辑************************
    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        self.pen = QPen(self.penColor, self.penSize, Qt.SolidLine)
        self.painter.setPen(self.pen)

        if len(self.pos_xy) > 1:
            point_start = self.pos_xy[0]
            for pos_tmp in self.pos_xy:
                point_end = pos_tmp

                if point_end == (-1, -1):
                    point_start = (-1, -1)
                    continue
                if point_start == (-1, -1):
                    point_start = point_end
                    continue

                self.painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                point_start = point_end

        self.painter.end()

    def mouseMoveEvent(self, event: QMouseEvent):
        """
        按住鼠标移动事件：将当前点添加到pos_xy列表中
        调用update()函数在这里相当于调用paintEvent()函数
        每次update()时，之前调用的paintEvent()留下的痕迹都会清空
        """
        # 中间变量pos_tmp提取当前点
        pos_tmp = (event.pos().x(), event.pos().y())
        self.pos_xy.append(pos_tmp)

        self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        重写鼠标按住后松开的事件
        在每次松开后向pos_xy列表中添加一个断点(-1, -1)
        然后在绘画时判断一下是不是断点就行了
        是断点的话就跳过去，不与之前的连续
        """
        pos_breaking = (-1, -1)
        self.pos_xy.append(pos_breaking)

        self.update()

    def cancel(self):
        """
        撤销操作
        :return:
        """
        pass

    def resume(self):
        """
        恢复操作
        :return:
        """

    def clear(self):
        """
        清空操作
        :return:
        """
        self.pos_xy.clear()
