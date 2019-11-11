# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 733)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.IconLabel = QtWidgets.QLabel(Form)
        self.IconLabel.setGeometry(QtCore.QRect(31, 34, 51, 41))
        self.IconLabel.setObjectName("IconLabel")
        self.TextLabel = QtWidgets.QLabel(Form)
        self.TextLabel.setGeometry(QtCore.QRect(110, 40, 72, 31))
        self.TextLabel.setObjectName("TextLabel")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 100, 181, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 170, 181, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(10, 240, 181, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(10, 310, 181, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(10, 380, 181, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(10, 450, 181, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(30, 690, 141, 16))
        self.messageLabel.setObjectName("messageLabel")
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(10, 530, 181, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.IconLabel.setText(_translate("Form", "TextLabel"))
        self.TextLabel.setText(_translate("Form", "TextLabel"))
        self.messageLabel.setText(_translate("Form", "TextLabel"))
