# coding:utf-8
"""
nonlocal && global
1、python引用变量的顺序为： 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量
2、global关键字用来在函数或其它局部作用域中使用全局变量
3、nonlocal关键字用来在函数或其它作用域中使用外层（非全局）变量
"""

global_var = 8


def get_number():
    # keyword global_var is unnecessary here
    print(global_var)


def change_num():
    # keyword global_var is must here
    global global_var
    global_var = global_var + 1


get_number()
change_num()
change_num()
get_number()


def print_obj_info():
    """
    for debug print
    :return:
    """
    num = 1

    def get_info(obj):
        nonlocal num
        print('[%d]:' % num, type(obj), obj)
        num += 1
    return get_info


get_info = print_obj_info()
get_info(global_var)
get_info(global_var)
get_info(global_var)
