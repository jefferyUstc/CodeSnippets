
class A(object):
    def __dir__(self):
        print('不给你看这个函数有什么属性和方法，哼、、哼哼')
        return []


if __name__ == "__main__":
    a = A()
    result = dir(a)
    print(result)
