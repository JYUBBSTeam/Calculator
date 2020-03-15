# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
    @Project -> File  : Calculator -> calculator
    @创建人：Liang
    @创建时间：2019/7/21
    @最后一次编辑时间：
    @描述：标准计算窗口设置
    @类：calculator
    @函数：
"""

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QSize, Qt, QRegExp

from Calculator.Sourse.Window.commomHelper.commomHelper_loadQss.commomHelper_Qss import CommonhelperQss
from Calculator.Sourse.Window.childWindow.calculatorWindow.UIdesigne.const.standardCalculator_const import Const


class Standardcalculator(QWidget):
    """
    标准计算器
    """

    def __init__(self):
        super(Standardcalculator, self).__init__()
        self.setObjectName('calculator')

        self.flag = True

        self.setup_ui()
        self.result_clear()

    def setup_ui(self):
        """

        :return:
        """
        reg = QRegExp("^$")  # 把键盘禁用了，仅可以按钮的输入
        validator = QRegExpValidator(reg, self)

        # 显示屏
        self.display = QLineEdit('0', self)  # 这个display就是显示屏，显示结果
        self.display.resize(self.width(), Const.DISPLAY_HEIGHT)
        self.display.setObjectName('display')
        self.display.setFont(QFont("Times", Const.FONT_SIZE))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setValidator(validator)
        self.display.setReadOnly(self.flag)
        self.display.setMaxLength(Const.MAXLENGTH)

        # 存储器操作按钮
        self.MC_btn = QPushButton("MC")
        self.MR_btn = QPushButton("MR")
        self.M_ADD_btn = QPushButton("M+")
        self.M_SUB_btn = QPushButton("M-")
        self.MS_btn = QPushButton("MS")
        self.M_btn = QPushButton("M^")

        # 加载布局
        self.set_base_layout()

    def set_base_layout(self):
        """
        布局
        :return:
        """

        # 垂直布局
        v_box_layout = QVBoxLayout()

        # 网格布局1
        grid_1 = QGridLayout()
        grid_1.addWidget(self.MC_btn, 0, 0)
        grid_1.addWidget(self.MR_btn, 0, 1)
        grid_1.addWidget(self.M_ADD_btn, 0, 2)
        grid_1.addWidget(self.M_SUB_btn, 0, 3)
        grid_1.addWidget(self.MS_btn, 0, 4)
        grid_1.addWidget(self.M_btn, 0, 5)

        # 网格布局2
        grid_2 = QGridLayout()

        names = ['%', 'CE', 'C', 'Del',
                 '1/x', 'x²', '√', '/',
                 '7', '8', '9', 'X',
                 '4', '5', '6', '-',
                 '1', '2', '3', '+',
                 '+/-', '0', '.', '=']

        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3),
               (4, 0), (4, 1), (4, 2), (4, 3),
               (5, 0), (5, 1), (5, 2), (5, 3)]

        # 记录添加控件的序号
        self.ORDER_NUMBER = 0

        for name in names:
            self.button = QPushButton(name)
            self.button.setObjectName('button')
            self.button.setFixedSize(QSize(Const.BUTTON_WIDTH, Const.BUTTON_HEIGHT))
            # self.button.clicked.connect(self.setCaculatorText)

            # 往网格布局里添加按钮
            grid_2.addWidget(self.button, pos[self.ORDER_NUMBER][0] + 1, pos[self.ORDER_NUMBER][1])

            self.ORDER_NUMBER += 1

        # #######################################################
        # 嵌套布局
        #
        v_box_layout.addWidget(self.display)
        v_box_layout.addLayout(grid_1)
        v_box_layout.addLayout(grid_2)

        v_box_layout.setContentsMargins(Const.CONTENTSMARGINS, Const.CONTENTSMARGINS, Const.CONTENTSMARGINS,
                                        Const.CONTENTSMARGINS)  # 调整布局与边界距离

        self.setLayout(v_box_layout)

    def load_qss(self):
        """
         加载Qss样式表
        :return:
        """

        self.styleFile = './Window/childWindow/calculatorWindow/Qss/calculatorWindow.qss'
        self.qssStyle = CommonhelperQss.read_qss(self.styleFile)
        self.setStyleSheet(self.qssStyle)

    def result_clear(self):
        """
        清空函数
        :return:
        """
        self.display.clear()
        self.display.setText('0')
        self.result = 0

    # #########################计算算法 #######################开始
    # '''
    #     用C++写，再用python模块调用C++代码
    # '''
    # 未完成
    @staticmethod
    def plus(num_1, num_2):
        """
        加法
        :param num_1:
        :param num_2:
        :return:
        """
        return num_1 + num_2

    @staticmethod
    def sub(num_1, num_2):
        """
        减法
        :param num_1:
        :param num_2:
        :return:
        """
        return num_1 - num_2

    @staticmethod
    def time(num_1, num_2):
        """
        乘法
        :param num_1:
        :param num_2:
        :return:
        """
        return num_1 * num_2

    @staticmethod
    def devide(num_1, num_2):
        """
        除法
        :param num_1:
        :param num_2:
        :return:
        """
        return num_1 / num_2

    # #########################计算算法 #######################结束
    # 判断是否是数字
    @staticmethod
    def is_number(sender_text):
        """

        :param sender_text:
        :return:
        """
        try:
            float(sender_text)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(sender_text)
            return True
        except (TypeError, ValueError):
            pass
            return False

    # 列表转换为字符串
    def change_array_to_string(self):
        """

        :return:
        """
        # str = ''.join(self.dis_Text)
        # return str
        pass
