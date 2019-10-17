"""
1、zip
一旦其中某个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致
"""

x = [1, 5, 4, 2]
y = [101, 78, 37, 15, 62, 99]
for _x, _y in zip(x,y):
    print(_x, _y, sep='\t')

"""
2、itertools.zip_longest()
以最长的来迭代
"""
import itertools

x = [1, 5, 4, 2]
y = [101, 78, 37, 15, 62, 99]
for _x, _y in itertools.zip_longest(x, y, fillvalue=None):
    print(_x, _y, sep='\t')

"""
3、zip函数哎呦一个用处是生成字典
"""
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
