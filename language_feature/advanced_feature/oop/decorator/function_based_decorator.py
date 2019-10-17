"""
1、装饰器函数其实是这样一个接口约束，它必须接受一个 callable 对象作为参数，然后返回一个 callable 对象
2、装饰器的作用就是为已经存在的函数或对象添加额外的功能
"""
# -------------------------------basic----------------------------------------------
# ----------------------------------------------------------------------------------


def log_it(func):
    def wrapper(*args, **kwargs):
        print("[Debug]: enter function {}()".format(func.__name__))
        return func(*args, **kwargs)  # if function func has return, remember to return

    return wrapper


@log_it
def add_number(*args):
    return sum(args)


print(add_number(1, 2, 3, 4))  # 10
print(add_number.__name__)  # wrapper


# -------------------------------带参数的装饰器----------------------------------------
# -----------------------------------------------------------------------------------


def log_it2(level='Debug'):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@log_it2(level='Info')
def add_number2(*args):
    return sum(args)


print(add_number2(1, 2, 3, 4, 5))
print(add_number2.__name__)

