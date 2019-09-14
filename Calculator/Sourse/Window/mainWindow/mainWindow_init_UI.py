'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：主窗口UI设计
    类：mainWindow_static_data:主窗口参数设置
        init_UI:主窗口参数初始化
    函数：
'''


class mainWindow_static_data:
    '''
        设置主窗口位置和大小
    '''
    x = 250
    y = 150
    width = 1400
    height = 750


class init_UI:
    '''
       主窗口参数初始化
    '''
    def initUI(self):
        # 窗口参数设置
        self.setGeometry(mainWindow_static_data.x, mainWindow_static_data.y, mainWindow_static_data.width,
                         mainWindow_static_data.height)
        self.setObjectName('mainWindow')