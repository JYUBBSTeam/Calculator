'''
    创建人：Liang
    创建时间：2019/7/25
    最后一次编辑时间：
    描述：窗口UI设计
    类: Action
    函数：
'''

from PyQt5.QtWidgets import QAction, QMenu
from PyQt5.QtGui import QIcon

class Action:
    def action_1(self, action, qIcon, textTip, shortCut, statusTip, _Menu):
        action = QAction(QIcon(qIcon), textTip, self)
        action.setShortcut(shortCut)
        action.setStatusTip(statusTip)
        _Menu.addAction(action)
        return action

    def action_2(self, action, textTip, shortCut, statusTip, _Menu):
        action = QAction(textTip, self)
        action.setShortcut(shortCut)
        action.setStatusTip(statusTip)
        _Menu.addAction(action)
        return action

    def action_3_a(self, action, qIcon, textTip, shortCut, statusTip):
        # 二级菜单下命令属性设置
        action = QAction(QIcon(qIcon), textTip, self)
        action.setShortcut(shortCut)
        action.setStatusTip(statusTip)
        return action
    def action_3_b(self, action, textTip, shortCut, statusTip):
        # 二级菜单下命令属性设置
        action = QAction(textTip, self)
        action.setShortcut(shortCut)
        action.setStatusTip(statusTip)
        return action

    def action_3_c(self, secondMenu, textTip, statusTip, _Menu):
        # 新增二级菜单
        secondMenu = QMenu(textTip, self)
        secondMenu.setStatusTip(statusTip)
        _Menu.addMenu(secondMenu)
        return secondMenu

    def action_3_d(self, secondMenu, textTip, _Menu):
        # 新增二级菜单
        secondMenu = QMenu(textTip, self)
        _Menu.addMenu(secondMenu)