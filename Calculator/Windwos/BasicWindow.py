from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)
        mainWindow.resize(500, 400)

        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")

        mainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle('四则运算')


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
