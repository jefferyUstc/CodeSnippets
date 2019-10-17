class Test(object):
    def __index__(self):
        return self.__int__(3.5)

    def __int__(self, x):
        return round(x)


a = [1, 2, 3, 4, 5]
print(a[Test()])
