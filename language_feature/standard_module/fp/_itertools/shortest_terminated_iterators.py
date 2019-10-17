from itertools import accumulate, chain, compress, dropwhile, filterfalse, groupby, islice, \
    starmap, takewhile, tee, zip_longest
from collections import Iterable, Iterator

import math


# -----------------------accumulate------------------------------
def add(a, b):
    return a + b


def sub(a, b):
    return b - a


print(list(accumulate([1, 2, 3, 4, 5], func=add)))
print(list(accumulate([1, 2, 3, 4, 5], func=sub)))

# -----------------------chain-----------------------------------
_chain = chain('ABC', 'DEF', 'GHI')
assert isinstance(_chain, Iterator) is True, '_chain is Iterator'
assert isinstance(_chain, Iterable) is True, '_chain is also Iterator'
print(list(_chain))

print(list(chain.from_iterable(['123', '24', 'ABC'])))

# -----------------------compress---------------------------------
print(list(compress([1, 2, 3, 4], [True, True, False, True])))

# -----------------------dropwhile---------------------------------

print(list(dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5])))  # starting when pred fails

# -----------------------filterfalse------------------------------

print(list(filterfalse(lambda x: x < 3, [1, 2, 3, 4, 5])))  # get elements of seq where pred(elem) is false

# -----------------------takewhile--------------------------------

print(list(takewhile(lambda x: x < 3, [1, 2, 3, 4, 5])))  # seq[0], seq[1], until pred fails


# -----------------------groupby----------------------------------
def key_func(x):
    return len(x)


fruits = ['apple', 'banana', 'grape', 'pear', 'chestnut', 'orange']
fruits = sorted(fruits, key=key_func)  # 可以注释这句话查看不一样的效果
group = groupby(fruits, key=key_func)

for k, v in group:
    print('{0}:{1}'.format(k, list(v)))

# -----------------------islice-----------------------------------

for item in islice('ABCDEFGHIJKLMN', 2, 10):  # start & stop
    print(item, end='\t')
print()


# -----------------------starmap----------------------------------
def my_pow(x):
    return math.pow(x[0], x[1])


print(list(starmap(pow, [(2, 5), (3, 2), (10, 3)])))  # func(*seq[0])
print(list(map(my_pow, [(2, 5), (3, 2), (10, 3)])))  # func(seq[0])

# -----------------------tee--------------------------------------
iters = tee([1, 2, 3, 4], 2)
for iter_item in iters:
    print(list(iter_item), end=';')
print()

# -----------------------zip_longest------------------------------
for x, y in zip_longest([1, 1, 1, 1], [2, 2, 2], fillvalue=None):  # 于zip对比
    print('(%s, %s)' % (x, y), end='\t')
