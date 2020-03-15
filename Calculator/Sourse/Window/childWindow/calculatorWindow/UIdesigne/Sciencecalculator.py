# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
    Project -> File  : Calculator -> scienceCalculator
    创建人：Liang
    创建时间：2020/2/20
    最后一次编辑时间：
    描述：科学计算器窗口设计
    类：
    函数：
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QSize, Qt, QRegExp

# from Calculator.Sourse.Window.commomHelper.commomHelper_loadQss.commomHelper_Qss import CommonhelperQss
from Calculator.Sourse.Window.childWindow.calculatorWindow.UIdesigne.const.science_calculator_const import Const


class Sciencecalculator(QWidget):
    """
    科学计算器界面
    """

    def __init__(self):
        super(Sciencecalculator, self).__init__()
        self.setObjectName('Sciencecalculator')

        self.flag = True

        # UI设计
        self.setup_ui()

        # 加载样式表
        self.load_qss()

    def setup_ui(self):
        """
        UI设计
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
        self.DEG_btn = QPushButton("DEG")
        self.DEG_btn.setObjectName("DEG_btn")
        self.F_E_btn = QPushButton("F-E")
        self.F_E_btn.setObjectName("F_E_btn")
        self.MC_btn = QPushButton("MC")
        self.MC_btn.setObjectName("MC_btn")
        self.MR_btn = QPushButton("MR")
        self.MR_btn.setObjectName("MR_btn")
        self.M_ADD_btn = QPushButton("M+")
        self.M_ADD_btn.setObjectName("M_ADD_btn")
        self.M_SUB_btn = QPushButton("M-")
        self.M_SUB_btn.setObjectName("M_SUB_btn")
        self.MS_btn = QPushButton("MS")
        self.MS_btn.setObjectName("MS_btn")
        self.M_btn = QPushButton("M^")
        self.M_btn.setObjectName("M_btn")

        # 函数按钮
        self.circular_btn = QPushButton("三角学")  # 点击打开三角函数按钮框
        self.circular_btn.setObjectName("circular_btn")
        self.baseFunction_btn = QPushButton("函数")  # 函数
        self.baseFunction_btn.setObjectName("baseFunction_btn")

        self.circular_btn.clicked.connect(self.circular_btn_win)
        self.baseFunction_btn.clicked.connect(self.function_btn_win)

        # 加载布局
        self.setbase_layout()

    def setbase_layout(self):
        """
        布局
        :return:
        """
        # 垂直布局
        v_box_layout = QVBoxLayout()

        # 网格布局1
        grid_1 = QGridLayout()
        grid_1.addWidget(self.DEG_btn, 0, 0)
        grid_1.addWidget(self.F_E_btn, 0, 1)
        grid_1.addWidget(self.MC_btn, 2, 0)
        grid_1.addWidget(self.MR_btn, 2, 1)
        grid_1.addWidget(self.M_ADD_btn, 2, 2)
        grid_1.addWidget(self.M_SUB_btn, 2, 3)
        grid_1.addWidget(self.MS_btn, 2, 4)
        grid_1.addWidget(self.M_btn, 2, 5)
        grid_1.addWidget(self.circular_btn, 3, 0, 1, 2)  # 占据两个按钮位置
        grid_1.addWidget(self.baseFunction_btn, 3, 2, 1, 2)  # 占据两个按钮位置
        # 网格布局2
        grid_2 = QGridLayout()

        names = ['2nd', 'PI', 'e', 'C', 'Del',
                 'x²', '1/x', '∣x∣', 'exp', 'mod',
                 'x³', '(', ')', 'n!', '/',
                 'xⁿ', '7', '8', '9', 'X',
                 '10ⁿ', '4', '5', '6', '-',
                 '㏒', '1', '2', '3', '+',
                 '㏑', '+/-', '0', '.', '=']

        pos = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
               (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
               (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
               (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
               (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),
               (6, 0), (6, 1), (6, 2), (6, 3), (6, 4)]

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

        # 使用嵌套布局
        v_box_layout.addWidget(self.display)
        v_box_layout.addLayout(grid_1)
        v_box_layout.addLayout(grid_2)

        v_box_layout.setContentsMargins(Const.CONTENTSMARGINS, Const.CONTENTSMARGINS, Const.CONTENTSMARGINS,
                                        Const.CONTENTSMARGINS)  # 调整布局与边界距离

        self.setLayout(v_box_layout)

    def circular_btn_win(self):
        """
        三角函数按钮框
        :return:
        """
        self.circular_Win = QWidget(self)
        self.circular_Win.setObjectName("circular_Win")
        self.circular_Win.setFixedSize(400, 200)
        self.circular_Win.move(80, 175)
        self.circular_Win.setStyleSheet('background-color:white')

        # 三角函数框界面按钮
        self.two_nd_btn = QPushButton('2nd')
        self.two_nd_btn.setObjectName('two_nd_btn')
        self.sin_btn = QPushButton('sin')
        self.sin_btn.setObjectName('sin_btn')
        self.cos_btn = QPushButton('cos')
        self.cos_btn.setObjectName('cos_btn')
        self.tan_btn = QPushButton('tan')
        self.tan_btn.setObjectName('tan_btn')
        self.hyp_btn = QPushButton('hyp')
        self.hyp_btn.setObjectName('hyp_btn')
        self.sec_btn = QPushButton('sec')
        self.sec_btn.setObjectName('sec_btn')
        self.csc_btn = QPushButton('csc')
        self.csc_btn.setObjectName('csc_btn')
        self.cot_btn = QPushButton('cot')
        self.cot_btn.setObjectName('cot_btn')

        # 关闭按钮
        self.circular_Win_quit_btn = QPushButton('关闭')
        self.circular_Win_quit_btn.setObjectName('circular_Win_quit_btn')

        # 布局
        btn_grid_1 = QGridLayout()
        btn_grid_1.addWidget(self.two_nd_btn, 0, 0)
        btn_grid_1.addWidget(self.sin_btn, 0, 1)
        btn_grid_1.addWidget(self.cos_btn, 0, 2)
        btn_grid_1.addWidget(self.tan_btn, 0, 3)
        btn_grid_1.addWidget(self.hyp_btn, 1, 0)
        btn_grid_1.addWidget(self.sec_btn, 1, 1)
        btn_grid_1.addWidget(self.csc_btn, 1, 2)
        btn_grid_1.addWidget(self.cot_btn, 1, 3)
        btn_grid_1.addWidget(self.circular_Win_quit_btn, 3, 0, 1, 4)

        self.circular_Win.setLayout(btn_grid_1)

        # 槽函数连接
        self.circular_Win_quit_btn.clicked.connect(self.circular_win_to_quit)

        # 显示
        self.circular_Win.show()

    def function_btn_win(self):
        """
        函数按钮框
        :return:
        """
        self.function_win = QWidget(self)
        self.function_win.setObjectName("function_btn_win")
        self.function_win.setFixedSize(300, 200)
        self.function_win.move(400, 175)
        self.function_win.setStyleSheet('background-color:white')

        # 函数框界面按钮
        self.x_one_btn = QPushButton('')
        self.x_one_btn.setObjectName('')
        self.x_two_btn = QPushButton('')
        self.x_two_btn.setObjectName('')
        self.x_three_btn = QPushButton('')
        self.x_three_btn.setObjectName('')
        self.rand_btn = QPushButton('rand')
        self.rand_btn.setObjectName('rand_btn')
        self._dns_btn = QPushButton('->dns')
        self._dns_btn.setObjectName('_dns_btn')
        self._deg_btn = QPushButton('->deg')
        self._deg_btn.setObjectName('_deg_btn')

        # 关闭按钮
        self.function_Win_quit_btn = QPushButton('关闭')
        self.function_Win_quit_btn.setObjectName('function_Win_quit_btn')

        # 布局
        btn_grid_2 = QGridLayout()
        btn_grid_2.addWidget(self.x_one_btn, 0, 0)
        btn_grid_2.addWidget(self.x_two_btn, 0, 1)
        btn_grid_2.addWidget(self.x_three_btn, 0, 2)
        btn_grid_2.addWidget(self.rand_btn, 1, 0)
        btn_grid_2.addWidget(self._dns_btn, 1, 1)
        btn_grid_2.addWidget(self._deg_btn, 1, 2)
        btn_grid_2.addWidget(self.function_Win_quit_btn, 3, 0, 1, 3)

        self.function_win.setLayout(btn_grid_2)

        # 槽函数连接
        self.function_Win_quit_btn.clicked.connect(self.function_win_to_quit)

        # 显示
        self.function_win.show()

    # ####################################### 【业务逻辑】 ##########################################

    def load_qss(self):
        """
        加载Qss样式表
        :return:
        """
        pass
        # styleFile = ''
        # qssStyle = CommonHelper_qss.readQss(styleFile)
        # self.setStyleSheet(qssStyle)

    def circular_win_to_quit(self):
        """
        关闭三角函数框
        :return:
        """
        self.circular_Win.hide()

    def function_win_to_quit(self):
        """
        关闭函数框
        :return:
        """
        self.function_win.hide()

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
    #
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
    @staticmethod
    def is_number(sender_text):
        """
        判断是否是数字
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

    @staticmethod
    def change_array_to_string(dis_text):
        """
        列表转换为字符串
        :return:
        """
        _str = ''.join(dis_text)
        return _str


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Sciencecalculator()
    win.show()

    sys.exit(app.exec_())
