# ----------------------------form1------------------------------------------------
# ---------------------------------------------------------------------------------


class Person:
    def __init__(self, first_name):
        self.first_name = first_name
        # self._first_name = first_name  # also ok

    @property
    def first_name(self):
        return self._first_name
        # return self.first_name  # not ok

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        del self._first_name


person = Person("jeffery")
print(person.first_name)
person.first_name = 'jeffery520'
print(person.first_name)
del person.first_name
print('ok')

# ----------------------------form2------------------------------------------------
# ---------------------------------------------------------------------------------


class Person2:
    def __init__(self, first_name):
        self.first_name = first_name

    def get_name(self):
        return self._first_name

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_name(self):
        del self._first_name

    first_name = property(get_name, set_name, del_name)


person = Person2("jeffery")
print(person.first_name)
person.first_name = 'jeffery520'
print(person.first_name)
del person.first_name

# ----------------------------可能的最佳操作------------------------------------------------
# ---------------------------------------------------------------------------------


class Person3:
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name
        # return self.first_name  # not ok

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        del self._first_name


person = Person3("jeffery")
print(person.first_name)
print(person._first_name)
person.first_name = 'jeffery520'
person._first_name = 'jeffery520'
del person.first_name
print('ok')


# ----------------------------可能的最佳操作------------------------------------------------
# ---------------------------------------------------------------------------------


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @score.deleter
    def score(self):
        del self._score
