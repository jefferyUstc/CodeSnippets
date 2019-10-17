from operator import attrgetter


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return self.name

    __repr__ = __str__


students = [
    Student('jane', 96, 12),
    Student('john', 95, 12),
    Student('dave', 98, 10),
]

print(sorted(students, key=attrgetter('age')))
print(sorted(students, key=lambda o: o.age))
print(sorted(students, key=attrgetter('age', 'grade'), reverse=True))

import locale
locale.strcoll