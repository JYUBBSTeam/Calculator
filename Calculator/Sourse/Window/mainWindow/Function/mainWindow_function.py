'''
    创建人：Liang
    创建时间：2019.9.17
    最后一次编辑时间：
    描述：
    类:
    函数：
'''


from PyQt5.QtWidgets import QFileDialog


from Calculator.Calculator.Sourse.Window.mainWindow.mainWindow_setup_UI import setupUI

class function(setupUI):
    def __init__(self):
        super(function, self).__init__()

    # 最小化窗口
    def ShowMininizedWindow(self):
        self.showMinimized()

    # 最大化窗口
    def ShowMaximizedWindow(self):
        self.showMaximized()

    # 复原窗口
    def ShowRestoreWindow(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    # 关闭窗口
    def CloseWindow(self):
        self.close()