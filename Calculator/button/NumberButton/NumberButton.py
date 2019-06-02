from button.BasicButton.button import basic_button
from PyQt5.QtCore import QFile
import sys
from PyQt5 import QtCore


class number_button(basic_button):
    myChar = None

    def __init__(self, character):
        super().__init__(character)
        self.myChar = character

        qss_file = QFile("QSS/NumberButtonStyle.qss")
        qss_file.open(QFile.ReadOnly)
        if qss_file.isOpen():
            qss_stream = QtCore.QTextStream(qss_file).readAll()
            self.setStylesheet(qss_stream)
        else:
            # 退出值为1说明打开qss失败
            sys.exit(1)

    def click_connect(self, number_string):
        self.clicked.connect(self.add_number(number_string))

    def add_number(self, number_string):
        if number_string == "0" and self.myChar == "0":
            return number_string
        else:
            number_string = number_string + self.myChar
            return number_string
