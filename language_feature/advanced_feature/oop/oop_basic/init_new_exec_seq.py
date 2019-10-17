class A(object):
    def __new__(cls, *args, **kwargs):
        print('A __new__')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('A __init__')


class B(A):
    def __new__(cls, *args, **kwargs):
        print('B __new__')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('B __init__')
        super().__init__()


if __name__ == '__main__':
    b = B()
