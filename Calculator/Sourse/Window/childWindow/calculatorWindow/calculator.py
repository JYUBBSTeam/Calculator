# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @Project -> File  : Calculator -> calculator
    @创建人：Liang
    @创建时间：2019/7/21
    @最后一次编辑时间：
    @描述：计算窗口设置
    @类：calculator
    @函数：
'''

import const    # 导入常量模块
from PyQt5.QtWidgets import QWidget, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QGridLayout,QLineEdit, QTextEdit, QButtonGroup
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QSize, Qt, QRegExp

const.NUM_1 = 48
const.NUM_2 = 58
const.DISPLAY_HEIGHT = 40
const.FONT_SIZE = 20
const.MAXLENGTH = 200
const.BUTTON_WIDTH = 85
const.BUTTON_HEIGHT = 50
const.CONTENTSMARGINS = 11

class calculator(QWidget):
    '''

    '''
    def __init__(self):
        super(calculator, self).__init__()
        self.setObjectName('calculator')
        # self.resize(1046, 704)

        self.dis_Text = []  # 储存算式字符
        self.dis_TextSubscript = -1 # 记录下标，-1为空
        self.disTextTop = ''

        # 初始化栈
        self.char_stack = []  # 操作符号的栈
        self.num_stack = []  # 操作数的栈

        self.nums = [chr(i) for i in range(const.NUM_1, const.NUM_2)]  # 用于判断按钮 的值是否是数字   chr(i)用一个整数做参数，返回一个对应的字符
        self.operators = ['+', '-', '×', '÷']  # 用于判断按钮的值是否是操作符

        self.empty_flag = True  # flag是用来判断计算器是不是第一次启动，在显示屏中无数据
        self.after_operator = False  # 比如1+2输入+后，1还显示在屏幕上，输入了2之后，1就被代替了，这个flag的作用就是这样

        self.char_top = ''  # 保留栈顶的操作符号
        self.num_top = 0  # 保留栈顶的数值
        self.result = 0  # 保留计算结果， 看计算器计算一次后，再继续按等号，还会重复 最近一次计算

        # # 各种操作符输入情况（'>'取前面一个操作符，'<'取后面一个操作符
        # self.priority_map = {
        #     '++': '>', '+-': '>', '-+': '>', '--': '>',
        #     '+*': '<', '+/': '<', '-*': '<', '-/': '<',
        #     '**': '>', '//': '>', '*+': '>', '/+': '>',
        #     '*-': '>', '/-': '>', '*/': '>', '/*': '>',
        # }

        self.setup_UI()
        self.resultClear()
        self.calculatorDisplayClear()

    def setup_UI(self):
        '''

        :return:
        '''
        reg = QRegExp("^$")  # 把键盘禁用了，仅可以按钮的输入
        validator = QRegExpValidator(reg, self)

        self.display = QLineEdit('0', self)  # 这个display就是显示屏，显示结果
        self.display.resize(self.width(), const.DISPLAY_HEIGHT)
        self.display.setObjectName('display')
        self.display.setFont(QFont("Times", const.FONT_SIZE))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setValidator(validator)
        self.display.setReadOnly(True)
        self.display.setMaxLength(const.MAXLENGTH)

        # 垂直布局
        VBoxLayout = QVBoxLayout()

        # 水平布局
        HBoxLayout = QHBoxLayout()

        # 网格布局
        grid = QGridLayout()

        names = ['7', '8', '9', 'PI', 'e', 'AC', 'Del',
                 '4', '5', '6', '.', '%', '+', '-',
                 '1', '2', '3', '0', '=', '*', '/',
                 '', '', '', '', '', '', '',
                 '(', ')', '√', '∑', 'lg', 'cot', 'acot',
                     'x!', '1/x', 'x²', 'x³', '∫', '∬', '∭',
                 'log', '㏑', 'tan', 'atan', '∮', '∯', '∰',
                 'cosh', 'sinh', 'cos', 'acos', '∂', 'sin', 'asin']
        pos = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
               (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
               (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
               (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
               (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
               (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
               (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
               (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6),
               (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6)]

        ####################设置单选按钮####################开始
        # 将单选按钮添加到分组 bg1 中,同时分配ID号
        self.bg1 = QButtonGroup(self)
        self.qRadioButton_1 = QRadioButton('弧度')
        self.qRadioButton_2 = QRadioButton('角度')
        self.bg1.addButton(self.qRadioButton_1, 1)
        self.bg1.addButton(self.qRadioButton_2, 2)

        # 配置信号与槽函数
        # self.bg1.buttonClicked.connect(self.)
        # 未完成
        #

        ####################设置单选按钮####################结束

        # 记录添加控件的序号
        ORDER_NUMBER = 0

        for name in names:

            if ORDER_NUMBER == 21:
                grid.addWidget(self.qRadioButton_1, pos[ORDER_NUMBER][0] + 1, pos[ORDER_NUMBER][1])
            elif ORDER_NUMBER == 22:
                grid.addWidget(self.qRadioButton_2, pos[ORDER_NUMBER][0] + 1, pos[ORDER_NUMBER][1])
            elif ORDER_NUMBER in range(23, 28):
                pass
            else:
                self.button = QPushButton(name)
                self.button.setObjectName('button')
                self.button.setFixedSize(QSize(const.BUTTON_WIDTH, const.BUTTON_HEIGHT))
                self.button.clicked.connect(self.setCaculatorText)

                # 往网格布局里添加按钮
                grid.addWidget(self.button, pos[ORDER_NUMBER][0] + 1, pos[ORDER_NUMBER][1])

            ORDER_NUMBER = ORDER_NUMBER + 1

        # 创建多行文本显示框，用于显示计算过程
        self.calculator_display = QTextEdit()
        self.calculator_display.setObjectName('more_dispaly')
        self.calculator_display.setReadOnly(True)  # 只读
        self.calculator_display.setAlignment(Qt.AlignRight)

        ########################################################
        # 嵌套布局
        #
        HBoxLayout.addLayout(grid)
        HBoxLayout.addWidget(self.calculator_display)
        VBoxLayout.addWidget(self.display)
        VBoxLayout.addLayout(HBoxLayout)

        VBoxLayout.setContentsMargins(const.CONTENTSMARGINS, const.CONTENTSMARGINS, const.CONTENTSMARGINS, const.CONTENTSMARGINS)  # 调整布局与边界距离

        self.setLayout(VBoxLayout)

    ####################################################################################################################
    #  槽函数
    ####################################################################################################################
    #
    # 清空函数
    def resultClear(self):
        self.display.clear()
        self.display.setText('0')
        self.result = 0
    def calculatorDisplayClear(self):
        self.calculator_display.clear()
        self.empty_flag = True

    # 算式文本展示
    def setCaculatorText(self):
        '''

        :return:
        '''
        self.sender = self.sender()
        self.sender_text = self.sender.text()
        try:
            if self.empty_flag == True:
                self.disTextTop = self.sender_text
                self.dis_Text.append(self.disTextTop)
                self.dis_TextSubscript += 1
                self.empty_flag = False
            elif self.is_number(self.sender_text):
                self.disTextTop = self.sender_text
                self.dis_Text.append(self.disTextTop)
                self.dis_TextSubscript += 1
            elif self.sender_text in self.operators:
                if self.dis_Text[self.dis_TextSubscript - 1] in self.operators:
                    self.calculator_display.setToolTip("Error!!!")
                else:
                    self.disTextTop = self.sender_text
                    self.dis_Text.append(self.disTextTop)
                    self.dis_TextSubscript += 1
                # 未完成
            pass
            self.calculatorDisplayClear()
            # 展示算式文本
            self.calculator_display.setText(self.changeArrayToString())

        except TypeError:
            pass

    #####################################################################################################################
    #
    #
    #
    #########################计算算法 #######################开始
    '''
        用C++写，再用python模块调用C++代码
    '''
    # 未完成
    #########################计算算法 #######################结束
    # 判断是否是数字
    def is_number(self, senderText):
        '''

        :param senderText:
        :return:
        '''
        try:
            float(senderText)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(senderText)
            return True
        except (TypeError, ValueError):
            pass
            return False

    # 数组转换为字符串
    def changeArrayToString(self):
        str = ','.join(self.dis_Text)
        return str









