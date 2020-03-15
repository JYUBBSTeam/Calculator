# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
-----------------------------------
    @author: Liang
    @file: ImageScale.py
    @date: 2020/3/14
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/3/14
-----------------------------------
    @desc:
        自定义图片缩放公共类
----------------------------------- 
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon


class ImageScale:
    def __init__(self):
        super(ImageScale, self).__init__()

    def image_icon_scale(self, image_path, width, height):
        self.imagePath = image_path
        self.width = width
        self.heght = height

        self.pixmap = QPixmap(self.imagePath)
        # scaled()返回一个QPixmap
        self.fitPixmap = self.pixmap.scaled(self.width, self.heght, Qt.IgnoreAspectRatio)

        self.icon = QIcon(self.fitPixmap)

        # 返回图标
        return self.icon

    def pixmap_scale(self, image_path, width, height):
        self.imagePath = image_path
        self.width = width
        self.heght = height

        self.pixmap = QPixmap(self.imagePath)
        # scaled()返回一个QPixmap
        self.fitPixmap = self.pixmap.scaled(self.width, self.heght, Qt.IgnoreAspectRatio)

        # 返回QPixmap类型的图片
        return self.fitPixmap
