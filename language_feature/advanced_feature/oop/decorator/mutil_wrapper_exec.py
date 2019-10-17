def decorator_a(func):
    print('Get in decorator_a')

    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a


def decorator_b(func):
    print('Get in decorator_b')

    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b


@decorator_b
@decorator_a
def f(x):
    print('Get in f')
    return x * 2


res = f(1)
print('res:', res)


# Get in decorator_a
# Get in decorator_b
# Get in inner_b
# Get in inner_a
# Get in f
# res: 2
