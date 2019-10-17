#! /usr/bin/python
# _*_ coding: utf-8 _*_


class Test(object):
    def __init__(self, count):
        self.count = count

    def __getattr__(self, name):
        print('__getattr__')
        raise AttributeError('no such field')

    def __getattribute__(self, item):
        """
        一旦重载了 __getattribute__() 方法, 如果找不到属性,
        则必须要手动加入第④步, 否则无法进入到 第⑤步 (__getattr__)的
        :param item:
        :return:
        """

        print('__getattribute__')
        return super().__getattribute__(item)

    def __setattr__(self, name, value):
        print('__setattr__')
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print('__delattr__')
        super().__delattr__(name)


t = Test(3)
print(t.count)
print('*'*40)

t.x = 10  # __setattr__
a = t.x  # __getattribute__
print(a)  # 10

print('**', t.__dict__)
# __getattribute__
# ** {'x': 10}

if 'x' in t.__class__.__bases__[0].__dict__:
    print('** x in base class dict')
else:
    print('** x not in base class dict')
# __getattribute__
# ** x not in base class dict

del t.x  # __delattr__

a = t.x
# __getattribute__
# __getattr__
