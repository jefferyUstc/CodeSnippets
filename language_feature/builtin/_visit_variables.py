# -*- coding:utf-8 _*-  
""" 
@author:jeffery
@time: 2019/04/29 10:03
@contact: jeffery_cpu@163.com
"""

"""
当引用一个变量的时候，对这个变量的搜索是按以下顺序查找（LEGB）：
    本地作用域(Local)
    嵌套作用域(Enclosing function locals)==>nonlocal
    全局作用域(Global)==>global
    内置作用域(builtins模块)
"""

"""
locals()===>局部名称空间
globals()===>全局名称空间

    在全局名称空间下，globals()和locals()返回相同的字典。
    通过这两个函数，可以在局部名称空间中访问全局名称空间的变量
"""


def foo():
    num = 10
    # 在局部名称空间中访问全局名称空间的变量
    # output: ('foo globals-num', 5)
    print("foo globals-num", globals()['num'])

    # output: ('foo locals-num', 10)
    print("foo locals-num", locals()['num'])


num = 5
foo()

# 在全局名称空间下，globals()和locals()返回相同的字典。
print("globals", globals())
print("locals", globals())
