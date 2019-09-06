"""
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：主窗口(创建菜单栏、状态栏、工具栏）
    类: mainWindow:主窗口
"""

import sys
#import time    load_Message依赖此module，考虑删除

from PyQt5.QtWidgets import QApplication, qApp
from Calculator.Calculator.Window.mainWindow.mainWindow import mainWindow
from Calculator.Calculator.Window.commomHelper_loadQss.commomHelper_Qss import CommonHelper_qss
from Calculator.Calculator.Window.mainWindow.init_Splash import initSplash

# 启动界面显示时间的设置
"""
def load_Message(splash):
    for i in range(1, 5):  # 显示时间4秒
        time.sleep(0.5)  # 睡眠
        splash.setText("初始化程序...{0}%".format(25 * i))
        splash.update()
        qApp.processEvents()
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    """ 取消启动界面
    splash = initSplash()
    splash.show()
    qApp.processEvents()
    load_Message(splash)
    splash.close()  # 隐藏启动界面
    """

    main_Window = mainWindow()

    # 加载Qss样式表-
    styleFile = './mainWindow/Qss/mainWindow.qss'
    qssStyle = CommonHelper_qss.readQss(styleFile)
    main_Window.setStyleSheet(qssStyle)

    main_Window.show()

    sys.exit(app.exec_())
