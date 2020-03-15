# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiHistoryDialog(object):
    '''
    历史记录窗口
    '''

    def setup_ui(self, history_Dialog):
        '''

        :param history_Dialog:
        :return:
        '''
        history_Dialog.setObjectName("history_Dialog")
        history_Dialog.resize(600, 500)
        self.pushButton = QtWidgets.QPushButton(history_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(history_Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 110, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(history_Dialog)
        self.textEdit.setGeometry(QtCore.QRect(240, 0, 351, 491))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(history_Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 180, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close_win)

        self.retranslate_ui(history_Dialog)
        QtCore.QMetaObject.connectSlotsByName(history_Dialog)

    def retranslate_ui(self, history_Dialog):
        _translate = QtCore.QCoreApplication.translate
        history_Dialog.setWindowTitle(_translate("history_Dialog", "Dialog"))
        self.pushButton.setText(_translate("history_Dialog", "重置"))
        self.pushButton_2.setText(_translate("history_Dialog", "刷新"))
        self.textEdit.setHtml(_translate("history_Dialog",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\""
                                         " \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                         "/><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; "
                                         "font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                                         "\"><br /></p></body></html>"))
        self.pushButton_3.setText(_translate("history_Dialog", "退出"))

    def reset(self):
        '''
        重置
        :return:
        '''
        pass

    def freshe(self):
        '''
        刷新
        :return:
        '''
        pass

    def close_win(self):
        '''
         退出窗口
        :return:
        '''
        self.close()
