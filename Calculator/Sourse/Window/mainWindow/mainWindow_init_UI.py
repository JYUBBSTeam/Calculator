'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：主窗口UI设计
    类：init_UI:主窗口参数初始化
    函数：
'''


import const    # 导入常量模块

const.WIN_X = 250
const.WIN_Y = 150
const.WIN_WIDTH = 1400
const.WIN_HEIGHT = 750


class init_UI:
    '''
       主窗口参数初始化
    '''
    def initUI(self):
        # 窗口参数设置
        self.setGeometry(const.WIN_X, const.WIN_Y, const.WIN_WIDTH, const.WIN_HEIGHT)
        self.setObjectName('mainWindow')