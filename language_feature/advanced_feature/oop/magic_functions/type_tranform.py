class A(object):
    def __init__(self, num):
        self.x = num

    def __int__(self):
        pass

    def __float__(self):
        pass

    def __long__(self):
        pass

    def __complex__(self):
        pass

    def __bytes__(self):
        pass

    def __oct__(self):
        pass

    def __hex__(self):
        pass

    def __str__(self):
        pass

    def __nonzero__(self):
        if self.x != 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(bool(A(5)))
