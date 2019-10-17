import abc
# -----------------------------case01-----------------------------------
# ----------------------------------------------------------------------


class A(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, _input):
        pass

    @abc.abstractmethod
    def save(self, output, data):
        pass


class B(A):
    def load(self, _input):
        return _input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print(issubclass(B, A))
    print(isinstance(B(), A))
    print(A.__subclasses__())


# -----------------------------case02-----------------------------------
# ----------------------------------------------------------------------


class C(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        pass

    @classmethod
    def __subclasshook__(cls, _cls):
        print('class invoke ********')
        if cls is C:
            if any("say" in B.__dict__ for B in _cls.__mro__):
                return True
        return NotImplemented


class D(object):
    def say(self):
        print('function say implemented in subclass')


print(issubclass(D, C))
print(isinstance(D(), C))
print(C.__subclasshook__(D))

# class invoke ********
# True
# True

# True

# -----------------------------case03-----------------------------------
# ----------------------------------------------------------------------


class A(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    @property
    def value(self):
        return 'should never see this.'

    @value.setter
    def value(self, _value):
        return


class B(A):
    _value = 'default'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _value):
        self._value = _value


b = B()
print(b.value)  # 尝试访问实例b的_value属性，但b自己没有该属性，因此访问的是类的_value属性。
b.value = 'hello'  # 为实例b添加_value属性，初始值为'hello'
print(b.value)  # 访问实例b自己的_value属性


# -----------------------------case04-----------------------------------
# ----------------------------------------------------------------------


class A(object):
    __metaclass__ = abc.ABCMeta

    @property
    @abc.abstractmethod
    def value(self):
        pass

    @value.setter
    @abc.abstractmethod
    def value(self, _value):
        pass

    @classmethod
    @abc.abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abc.abstractmethod
    def method2():
        pass


class B(A):
    _value = 'default'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, _value):
        self._value = _value

    def method1(cls):
        print(type(cls))

    @staticmethod
    def method2():
        pass


b = B()
print(b.value)  # 尝试访问实例b的_value属性，但b自己没有该属性，因此访问的是类的_value属性。
b.value = 'hello'  # 为实例b添加_value属性，初始值为'hello'
print(b.value)  # 访问实例b自己的_value属性
