from _orm_dataType import Field


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print('*******__new__*******')
        # print(name)
        # print(bases)
        # print(attrs)
        # print('*******__new__*******')
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)  # 这里是创建类，不是创建对象

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return super().__new__(cls, name, bases, attrs)  # 这里是创建类，不是创建对象


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


if __name__ == '__main__':
    m = Model()

