'''
    创建人：Liang
    创建时间：2019/7/18
    最后一次编辑时间：
    描述：创建一个加载QSS样式表的公共类
    类：CommonHelper:加载QSS样式表的公共类
    函数：
'''


class CommonhelperQss:
    """
    加载样式表公共类
    """

    @staticmethod
    def read_qss(style_path):
        """

        :param style_path:
        :return:
        """
        with open(style_path, 'r') as f:
            return f.read()
