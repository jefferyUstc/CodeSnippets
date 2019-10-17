from functools import partial

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)


def update_wrapper(wrapper,
                   wrapped,
                   assigned=WRAPPER_ASSIGNMENTS,
                   updated=WRAPPER_UPDATES):
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
    # from the wrapped function when updating __dict__
    wrapper.__wrapped__ = wrapped
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper


def wraps(wrapped,
          assigned=WRAPPER_ASSIGNMENTS,
          updated=WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)


def log_it(func):
    @wraps(func)  # comment this line to see the diff
    def wrapper(*args, **kwargs):
        print("[Debug]: enter function {}()".format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@log_it
def add_number(*args):
    """
    add numbers in tuple
    :param args: should be numbers
    :return: the sum of tuple
    """
    return sum(args)


print(add_number.__name__, add_number.__doc__)
