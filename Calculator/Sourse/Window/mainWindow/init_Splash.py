# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：程序启动界面UI设计
    类：MySplash:自定义Splash类
    函数：
'''


import const # 导入常量模块
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QPaintEvent

const.SPLASH_X = 450
const.SPLASH_Y = 190
const.SPLASH_WIDTH = 1000
const.SPLASH_HEIGHT = 450
const.PIXMAP_X = 100
const.PIXMAP_Y = 100
const.TEXT_X = 350
const.TEXT_Y = 342
const.TEXT_WIDTH = 200
const.TEXT_HEIGHT = 100

# 自定义Splash类
class initSplash(QWidget):
    def __init__(self):
        super(initSplash, self).__init__()
        #self.setAttribute(Qt.WA_TranslucentBackground, True)    # 设置背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)     # 设置无边框
        self.setGeometry(const.SPLASH_X, const.SPLASH_Y, const.SPLASH_WIDTH, const.PLASH_HEIGHT)    # 设置窗口位置和大小
        self.text = "初始化程序...0%"

    # 重写绘画事件
    def paintEvent(self, QPaintEvent):
        self.p = QPainter(self)
        self.p.setPen(QPen())
        self.p.setBrush(QBrush())
        self.p.drawPixmap(const.PIXMAP_X, const.PIXMAP_Y, QPixmap("./image/history.jpg"))    # 加载图片
        self.p.drawText(QRect(const.TEXT_X, const.TEXT_Y, const.TEXT_WIDTH, const.TEXT_HEIGHT), Qt.AlignCenter, self.text)    #showMessage

    def setText(self, text):
        self.text = text
        self.paintEvent(QPaintEvent)



