'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：程序启动界面UI设计
    类：MySplash:自定义Splash类
    函数：
'''

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QPaintEvent

SPLASH_X = 450
SPLASH_Y = 190
SPLASH_WIDTH = 1000
SPLASH_HEIGHT = 450
PIXMAP_X = 100
PIXMAP_Y = 100
TEXT_X = 350
TEXT_Y = 342
TEXT_WIDTH = 200
TEXT_HEIGHT = 100

# 自定义Splash类
class initSplash(QWidget):
    def __init__(self):
        super(initSplash, self).__init__()
        #self.setAttribute(Qt.WA_TranslucentBackground, True)    # 设置背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)     # 设置无边框
        self.setGeometry(SPLASH_X, SPLASH_Y, SPLASH_WIDTH, SPLASH_HEIGHT)    # 设置窗口位置和大小
        self.text = "初始化程序...0%"

    # 重写绘画事件
    def paintEvent(self, QPaintEvent):
        self.p = QPainter(self)
        self.p.setPen(QPen())
        self.p.setBrush(QBrush())
        self.p.drawPixmap(PIXMAP_X, PIXMAP_Y, QPixmap("./QIcon/history.jpg"))    # 加载图片
        self.p.drawText(QRect(TEXT_X, TEXT_Y, TEXT_WIDTH, TEXT_HEIGHT), Qt.AlignCenter, self.text)    #showMessage

    def setText(self, text):
        self.text = text
        self.paintEvent(QPaintEvent)



