'''
    创建人：Liang
    创建时间：
    最后一次编辑时间：
    描述：
    类:
    函数：
'''


from PyQt5.QtWidgets import QFileDialog, QApplication

class function:
    # 打开文件
    def getFile(self):
        '''
            getOpenFileName():返回用户所选择文件的名称，并打开该文件
            第一个参数用于指定父组件
            第二个参数指定对话框标题
            第三个参数指定目录
            第四个参数是文件扩展名过滤器
        '''

        fname = QFileDialog.getOpenFileName(self, '选择文件', 'C:\\', "*.jpg *.gif *.png")

