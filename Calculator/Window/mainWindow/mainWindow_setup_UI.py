'''
    创建人：Liang
    创建时间：2019/7/25
    最后一次编辑时间：
    描述：窗口设置
    类: mainWindow_static_data:主窗口参数设置
        setupUI:窗口设置
'''


class mainWindow_static_data:
    '''
        设置主窗口位置和大小
    '''
    x = 250
    y = 150
    width = 1400
    height = 750


class setupUI:
    '''
        窗口设置
    '''

    def setup_Window(self):
        # 窗口参数设置
        self.setGeometry(mainWindow_static_data.x, mainWindow_static_data.y, mainWindow_static_data.width,
                         mainWindow_static_data.height)
        self.setObjectName('mainWindow')
