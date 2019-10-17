"""
当你想对不同的集合中所有元素执行某些操作的时候, 可以使用chain
chain() 接受一个或多个可迭代对象作为输入参数，然后创建一个迭代器，依次连续的返回每个可迭代对象中的元素。
这种方式要比先将序列合并再迭代要高效的多
"""

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
