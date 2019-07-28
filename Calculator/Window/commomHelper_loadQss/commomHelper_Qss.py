'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：创建一个加载QSS样式表的公共类
    类：CommonHelper:加载QSS样式表的公共类
'''


class CommonHelper_qss:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()