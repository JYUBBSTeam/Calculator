# !/usr/bin/env python
# _*_ coding: UTF-8 _*_
'''
-----------------------------------
    @author: Liang
    @file: actoinInterface.py
    @date: 2019/7/25
    @Software: PyCharm
-----------------------------------
    @Change Activity:
           2020/2/23
-----------------------------------
    @desc:
        实现添加菜单接口
----------------------------------- 
'''

# 抽象类加抽象方法等于面向编程中的接口
from abc import ABCMeta, abstractmethod


class ActionInterface(object):
    '''
    定义新增菜单接口
    '''
    __metaclass__ = ABCMeta  # 指定为抽象类

    @abstractmethod  # 抽象方法
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def action_b_2(self, _action, text_tip, short_cut, status_tip):
        '''
        二级菜单下命令属性设置
        :param _action:
        :param text_tip:
        :param short_cut:
        :param status_tip:
        :return:
        '''
        pass

    @abstractmethod
    def action_b_3(self, _second_menu, text_tip, status_tip, _menu):
        '''
        新增二级菜单
        :param _second_menu:
        :param text_tip:
        :param status_tip:
        :param _menu:
        :return:
        '''
        pass

    @abstractmethod
    def action_b_4(self, _second_menu, text_tip, _menu):
        '''
        新增二级菜单
        :param _second_menu:
        :param text_tip:
        :param _menu:
        :return:
        '''
        pass
