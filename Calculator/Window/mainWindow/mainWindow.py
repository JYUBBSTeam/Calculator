'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：主窗口(创建菜单栏、状态栏、工具栏）
    类：mainWindow_static_data：主窗口参数设置
        mainWindow:主窗口
'''

import sys
from idlelib import window

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, qApp

from Calculator.Window.childWindow.calculatorWindow.calculatorWindow import calculator_Window
from Calculator.Window.mainWindow.mainWindow_init_UI import init_UI
from Calculator.Window.loadQss.commomHelper_Qss import CommonHelper_qss
from Calculator.Window.mainWindow.init_Splash import initSplash

import time


class mainWindow(QMainWindow):
    '''
        主窗口
    '''
    def __init__(self):
        super().__init__()

        self.init_Ui()
        #self.setup_Ui()

    def init_Ui(self):
        self.init_Ui  = init_UI.initUI(self)

    def setup_Ui(self):
        #未完成
        pass
    
    def getFile(self):
        '''
            getOpenFileName():返回用户所选择文件的名称，并打开该文件
            第一个参数用于指定父组件
            第二个参数指定对话框标题
            第三个参数指定目录
            第四个参数是文件扩展名过滤器
        '''

        fname = QFileDialog.getOpenFileName(self, '选择文件', 'C:\\', "*.jpg *.gif *.png")

    def calculator_Win(self):
        self.calculator_Win = calculator_Window()

        self.calculator_Win.show()


#启动界面显示时间的设置
def load_Message(splash):
    for i in range (1, 5):  #显示时间4秒
        time.sleep(2)   #睡眠
        splash.setText("初始化程序...{0}%".format(25*i))
        splash.update()
        qApp.processEvents()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = initSplash()
    splash.show()
    qApp.processEvents()
    load_Message(splash)
    splash.close()  #隐藏启动界面

    main_Window = mainWindow()

    #加载Qss样式表-
    styleFile = 'Qss/mainWindow.qss'
    qssStyle = CommonHelper_qss.readQss(styleFile)
    main_Window.setStyleSheet(qssStyle)

    main_Window.show()

    sys.exit(app.exec_())
