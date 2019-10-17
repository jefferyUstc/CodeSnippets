# https://zhuanlan.zhihu.com/p/32764345
# -------------------------case01---------------------------------------------
# ----------------------------------------------------------------------------
# 描述器功能强大，应用广泛，它可以控制我们访问属性、方法的行为,
# 是@property、super、静态方法、类方法、甚至属性、实例背后的实现机制，是一种比较底层的设计


class M:
    def __init__(self, name, name2):
        print("descriptor init")
        self.name = name
        self.name2 = name2

    def __get__(self, instance, owner):
        """
        descriptor __get__ method, `self` means current instance of M
        :param instance: instance of Wrapper Class,, in this example ,it is instance of A
        :param owner: Wrapper Class, in this example ,it is A
        :return:
        """
        print('get第一个参数self: ', self.name)
        print('get第二个参数obj: ', instance.age)
        print('get第三个参数type: ', owner.name)
        return self.name

    def __set__(self, instance, value):
        """
        descriptor __set__ method, `self` means current instance of M
        :param instance: instance of Wrapper Class,, in this example ,it is instance of A
        :param value: the value to set
        :return:
        """
        print(instance.name)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        pass


class A:
    name = 'Bob'
    m = M('age', 'gender')

    def __init__(self, age):
        self.age = age


a = A(19)
print(a.age, '*' * 40, sep='\n')
print(a.m, '*' * 40, sep='\n')
a.m = 100
print(a.m, '*' * 40, sep='\n')
print(a.age, '*' * 40, sep='\n')


# -------------------------case02---------------------------------------------
# ----------------------------------------------------------------------------


class B:
    """
    实例直接调用时，类方法和实例方法都是bound method，而静态方法是function。
    因为静态方法本身就是定义在类里面的函数，所以不属于方法范畴
    """

    def print_name(self):
        print('print_name', self)

    @classmethod
    def print_class_name(cls):
        print('print_class_name')

    @staticmethod
    def print_static_name():
        print('print_static_name')


b = B()
B.__dict__['print_class_name'].__get__(None, B)()
B.__dict__['print_static_name'].__get__(None, B)()
B.__dict__['print_name'].__get__(b, B)()

b.print_class_name()
b.print_static_name()
b.print_name()


# -------------------------case03---------------------------------------------
# ----------------------------------------------------------------------------


class Property(object):

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


# 类似函数的形式
class A:
    def __init__(self, name, score):
        self.name = name  # 普通属性
        self.score = score

    def getscore(self):
        return self._score

    def setscore(self, value):
        print('setting score here')
        if isinstance(value, int):
            self._score = value
        else:
            print('please input an int')

    score = property(getscore, setscore)


a = A('Bob', 90)
print(a.name)  # 'Bob'
print(a.score)  # 90
a.score = 'bob'  # please input an int


# # 装饰器形式
class AA:
    def __init__(self, name, score):
        self.name = name  # 普通属性
        self.score = score

    @Property
    def score(self):
        print('getting score here')
        return self._score

    @score.setter
    def score(self, value):
        print('setting score here')
        if isinstance(value, int):
            self._score = value
        else:
            print('please input an int')


a = AA('Bob', 90)
print(a.name)  # 'Bob'
print(a.score)  # 90
a.score = 'bob'  # please input an int


# -------------------------case04(实际应用)---------------------------------------------
# ----------------------------------------------------------------------------


class Integer:
    """
    资料描述器和非资料描述器会产生不一样的优先级
    """

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(10, 11)