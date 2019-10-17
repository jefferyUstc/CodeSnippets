class A(object):
    def __init__(self):
        print('__init__')

    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super().__new__(cls, *args, **kwargs)  # cls表示一个类，一个当前要被实例化的类，参数由py解释器自动提供

    def __del__(self):
        print('__del__')


a = A()
print('do something')
# __new__
# __init__
# do something
# __del__

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        注意这实际上是一个类方法, cls 表示当前类
        :param args:
        :param kwargs:
        :return:
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


s1 = Singleton()
s2 = Singleton()
if s1 is s2:
    print('yeah')
