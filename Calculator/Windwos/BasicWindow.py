import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
if __name__=='__main__':
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(500,400)
    w.move(200,200)
    w.setWindowTitle('四则运算')
btn=QtWidgets.QPushButton('+',w)
btn.setGeometry(100,100,100,100)
btn.setToolTip('这是加法运算')
btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
w.show()
sys.exit(app.exec_())
