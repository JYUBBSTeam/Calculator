'''
    创建人：Liang
    创建时间：2019/7/25
    最后一次编辑时间：
    描述：窗口UI设计
    类: Action
    函数：
'''

from Calculator.Sourse.Window.mainWindow.QAction.actoinInterface import ActionInterface
from PyQt5.QtWidgets import QAction, QMenu
from PyQt5.QtGui import QIcon


class Action(ActionInterface):      # 继承自ActionInterface接口
    '''
    添加菜单模块
    '''

    def action_a_1(self, _action, q_icon, text_tip, short_cut, status_tip, _menu):
        '''
        新增一级菜单
        :param _action:
        :param q_icon:
        :param text_tip:
        :param short_cut:
        :param status_tip:
        :param _menu:
        :return:
        '''
        _action = QAction(QIcon(q_icon), text_tip, self)
        _action.setShortcut(short_cut)
        _action.setStatusTip(status_tip)
        _menu.addAction(_action)
        return _action

    def action_a_2(self, _action, text_tip, short_cut, status_tip, _menu):
        '''
        新增一级菜单
        :param _action:
        :param text_tip:
        :param short_cut:
        :param status_tip:
        :param _menu:
        :return:
        '''
        _action = QAction(text_tip, self)
        _action.setShortcut(short_cut)
        _action.setStatusTip(status_tip)
        _menu.addAction(_action)
        return _action

    def action_b_1(self, _action, q_icon, text_tip, short_cut, status_tip):
        '''
        二级菜单下命令属性设置
        :param _action:
        :param q_icon:
        :param text_tip:
        :param short_cut:
        :param status_tip:
        :return:
        '''
        _action = QAction(QIcon(q_icon), text_tip, self)
        _action.setShortcut(short_cut)
        _action.setStatusTip(status_tip)
        return _action

    def action_b_2(self, _action, text_tip, short_cut, status_tip):
        '''
        二级菜单下命令属性设置
        :param _action:
        :param text_tip:
        :param short_cut:
        :param status_tip:
        :return:
        '''
        _action = QAction(text_tip, self)
        _action.setShortcut(short_cut)
        _action.setStatusTip(status_tip)
        return _action

    def action_b_3(self, _second_menu, text_tip, status_tip, _menu):
        '''
        新增二级菜单
        :param _second_menu:
        :param text_tip:
        :param status_tip:
        :param _menu:
        :return:
        '''
        _second_menu = QMenu(text_tip, self)
        _second_menu.setStatusTip(status_tip)
        _menu.addMenu(_second_menu)
        return _second_menu

    def action_b_4(self, _second_menu, text_tip, _menu):
        '''
        新增二级菜单
        :param _second_menu:
        :param text_tip:
        :param _menu:
        :return:
        '''
        _second_menu = QMenu(text_tip, self)
        _menu.addMenu(_second_menu)
