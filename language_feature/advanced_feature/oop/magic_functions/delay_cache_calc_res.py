"""
描述器实现 lazy 计算
"""
import math


class LazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


# this func also replaceable for LazyProperty
def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


