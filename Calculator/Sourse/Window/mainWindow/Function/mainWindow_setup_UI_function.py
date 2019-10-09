'''
    创建人：Liang
    创建时间：
    最后一次编辑时间：
    描述：
    类:
    函数：
'''

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir


class function(QMainWindow):
    # 打开文件
    def getFile(self):
        '''
            getOpenFileName():返回用户所选择文件的名称，并打开该文件
            第一个参数用于指定父组件
            第二个参数指定对话框标题
            第三个参数指定目录
            第四个参数是文件扩展名过滤器
        '''

        fname, _ = QFileDialog.getOpenFileName(self, '选择图形文件', 'C:\\', "*.jpg *.gif *.png")
        self.pixmapLabel.setPixmap(QPixmap(fname))

    def getText(self):
        # 初始化实例，并设置一些参数
        # textDialog = QFileDialog()
        # textDialog.setFileMode(QFileDialog.AnyFile)
        # textDialog.setFilter(QDir.Files)
        textDialog = QFileDialog.getOpenFileName(self, '选择文本文件', 'C:\\', "*.txt *.doc *.docx")
        # 当选择器关闭的时候
        if textDialog.exec_():
            # 拿到所选择的文本
            filenames = textDialog.selectedFiles()
            # 读取文本内容设置到textEdit中
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
