'''
    创建人：Liang
    创建时间：2019/7/21
    最后一次编辑时间：
    描述：计算器
    类：init_UI:计算器UI设计
'''

from PyQt5.QtWidgets import QPushButton, QRadioButton, QGridLayout,QLineEdit, QButtonGroup
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QSize, Qt, QRegExp


class init_UI():
    '''
       计算器UI设计
    '''
    def init_Ui(self):

        self.setWindowTitle('计算器')

        reg = QRegExp("^$")     # 把键盘禁用了，仅可以按钮的输入
        validator = QRegExpValidator(reg, self)

        # 网格布局
        grid = QGridLayout()

        self.display = QLineEdit('0', self)     # 这个display就是显示屏
        self.display.setObjectName('display')
        self.display.setFont(QFont("Times", 20))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setValidator(validator)
        self.display.setReadOnly(True)
        self.display.setMaxLength(15)
        grid.addWidget(self.display, 0, 0, 1, 7)
        names = ['7', '8', '9', 'PI', 'e', 'AC', 'Del',
                 '4', '5', '6', '.', '%', '+', '-',
                 '1', '2', '3', '0', '=', '×', '÷',
                 '', '', '', '', '', '', '',
                 '(', ')', '√', '∑','lg', 'cot', 'acot',
                 'x!', '1/x', 'x²', 'x³', '∫', '∬', '∭',
                 'log', '㏑', 'tan', 'atan', '∮', '∯', '∰',
                  'cosh', 'sinh', 'cos', 'acos','∂', 'sin', 'asin',
                   '进制转换']
        pos = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
               (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
               (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
               (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
               (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
               (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
               (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
               (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6),
               (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6),
               (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6),]

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

        c = 0

        for name in names:


            if c == 21:
                grid.addWidget(self.qRadioButton_1, pos[c][0] + 1, pos[c][1])
            elif c == 22:
                grid.addWidget(self.qRadioButton_2,pos[c][0] + 1, pos[c][1])
            elif c in range (23, 28):
                pass
            else:
                button = QPushButton(name)
                button.setFixedSize(QSize(85, 50))
                # button.clicked.connect(self.未完成)

                # 往网格布局里添加按钮
                grid.addWidget(button, pos[c][0] + 1, pos[c][1])


            c = c + 1
            self.setLayout(grid)


