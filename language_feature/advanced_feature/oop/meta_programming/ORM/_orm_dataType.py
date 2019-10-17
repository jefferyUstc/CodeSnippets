class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super().__init__(name, 'bigint')
