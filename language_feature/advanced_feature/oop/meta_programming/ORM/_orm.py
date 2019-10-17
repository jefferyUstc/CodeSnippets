from _orm_dataType import IntegerField, StringField
from _orm_model import Model


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库
u.save()

# print(User.__bases__,  # 父类
#       User.__class__,  # 元类
#       User.__dict__,  # 字典
#       u.__class__  # 所属类
#       )
