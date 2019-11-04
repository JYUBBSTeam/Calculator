# !/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @创建人：Liang
    @创建时间：
    @最后一次编辑时间：
    @描述：创建常量公共类,
         请把常量类导入site-packages中！！！
    @类: _const；常量类
    @函数：
'''



# 常量类
class _const(object):
    class ConstError(TypeError) : pass
    class ConstCaseError(ConstError) : pass
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)"%name)
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const (%s)"%name)
        raise NameError(name)

import sys
sys.modules[__name__] = _const()