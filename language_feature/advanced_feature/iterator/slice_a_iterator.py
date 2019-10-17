from itertools import islice


def count(n=0):
    while True:
        yield n
        n = n + 1


if __name__ == '__main__':
    c = count(0)
    for x in islice(c, 10, 20):
        print(x)
