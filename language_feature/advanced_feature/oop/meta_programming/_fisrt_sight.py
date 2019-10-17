"""
编写能改变语言语法特性或者运行时特性的程序 | you write code that writes code.
"""


# 1
class A(object):
    def say_hello(self):
        print("Hello World!")


a = A()
print(type(a), type(A))  # <class '__main__.A'> <class 'type'>, 因此class的定义是运行时动态创建的，而创建class的方法就是使用type()函数


# 2
# type(object) -> the object's type
# type(name, bases, dict) -> a new type

def say_hello(self):
    print("Hello World!")


B = type('B', (object,), dict(say_hello=say_hello))
b = B()
b.say_hello()  # Hello World!


# 3
# 先定义metaclass，然后创建类，然后再创建实例。所以，metaclass允许你创建类或者修改类。
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    """
    元类就是重写新式类的实际构造方法__new__
    """

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return super().__new__(cls, name, bases, attrs)
        # return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


l = MyList()
l.add(1)
print(l)
