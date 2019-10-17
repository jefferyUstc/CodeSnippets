# -------------------------------basic----------------------------------------------
# ----------------------------------------------------------------------------------


class LogIt(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter function {func}()".format(
            func=self.func.__name__))
        return self.func(*args, **kwargs)


@LogIt
def add_number(*args):
    return sum(args)


# print(add_number(1, 2, 3, 4))
# print(add_number)


# -------------------------------带参数的装饰器----------------------------------------
# -----------------------------------------------------------------------------------


class LogIt2(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=self.level,
                func=func.__name__))
            return func(*args, **kwargs)
        return wrapper


@LogIt2(level='INFO')
def add_number2(*args):
    return sum(args)


print(add_number2(1, 2, 3, 4, 5))
print(add_number2.__name__)
