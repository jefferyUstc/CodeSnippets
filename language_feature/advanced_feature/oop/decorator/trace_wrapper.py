import linecache
import os
import sys


def trace(f):
    def globaltrace(frame, why, arg):
        if why == "call":
            return localtrace
        return None

    def localtrace(frame, why, arg):
        if why == "line":
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print("{}({}): {}".format(bname,
                                      lineno,
                                      linecache.getline(filename, lineno).strip('\r\n')))
        return localtrace

    def _f(*args, **kwds):
        sys.settrace(globaltrace)
        result = f(*args, **kwds)
        sys.settrace(None)
        return result

    return _f


@trace
def test():
    a = 1 + 1
    print(a)
    print(222)
    print(333)


test()
