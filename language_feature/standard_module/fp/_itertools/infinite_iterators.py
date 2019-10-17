from itertools import count, cycle, repeat
from collections import Iterable, Iterator, Generator

# -----------------------count-------------------------
for i in count(start=10, step=10):
    print(i)
    if i == 50:
        break


def count(firstval=0, step=1):
    """
    itertools.count函数等同于此实现
    """
    x = firstval
    while 1:
        yield x
        x += step


# -----------------------cycle-------------------------

for i, item in enumerate(cycle('ABCD')):
    if i == 10:
        break
    print(item, end='\t')

# -----------------------repeat------------------------

print('\n')
r = repeat('yeah', 9)
print(isinstance(r, Iterable))
print(isinstance(r, Iterator))
print(isinstance(r, Generator))

for i in range(10):
    try:
        print(next(r), end='\t')
    except StopIteration as e:
        print('\n', e)
