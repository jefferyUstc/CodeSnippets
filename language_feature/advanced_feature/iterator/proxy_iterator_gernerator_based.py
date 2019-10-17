def frange(start, stop, increment):
    x = start
    while x <= stop:
        yield x
        x += increment


if __name__ == '__main__':
    for i in frange(0, 4, 0.5):
        print(i)
