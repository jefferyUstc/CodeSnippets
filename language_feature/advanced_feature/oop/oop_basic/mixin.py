class Transportation(object):
    """
    交通工具的基类
    """
    pass


class FlyMixin(object):
    """
    Mixin 类，告诉其他人，这是一个"接口"，能够扩充类的某一个功能
    """
    def fly_able(self):
        pass


class Airliner(Transportation, FlyMixin):
    """
    客机
    """
    pass


class Helicopter(Transportation, FlyMixin):
    """
    直升机
    """
    pass
