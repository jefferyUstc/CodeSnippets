class A(object):
    def _pre_process(self):
        print('preoprocess data')

    def __call__(self, *args, **kwargs):
        self._pre_process()
        print('object called over')


A()()  # 调用了类中__call__()中的逻辑
