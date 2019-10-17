class Student(object):
    """
    Student class
    """

    # student_number是一个类属性, 可通过类访问，也可通过对象访问，所有对象共享该表量
    student_number = 0

    # 方法可有默认参数、可变参数、关键字参数和命名关键字参数
    def __init__(self, sid, name, score):
        """
        Student class init method
        """
        Student.student_number += 1
        self.__id = sid
        self.name = name
        self.score = score

    def print_info(self):
        """
        get Student info
        """
        print('%s: %s' % (self.name, self.score), end=' ')


class MasterStudent(Student):
    """
    MasterStudent class
    """
    def __init__(self, sid, name, score, major):
        """
        Student class init method
        """
        super().__init__(sid, name, score)
        self.major = major

    def print_info(self):
        """
        get Student score
        """
        super().print_info()  # 调用父类方法
        print('and majoring in %s' % self.major)

    def change_major(self, major):
        """
        change major
        """
        self.major = major


if __name__ == '__main__':
    ms = MasterStudent('001', 'jeffery', '90', 'bio')
    ms.print_info()
