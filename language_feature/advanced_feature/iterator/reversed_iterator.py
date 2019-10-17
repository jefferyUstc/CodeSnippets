"""
反向代理需要满足一下条件：
1、对象的大小可预先确定，如是一个列表 list_a = [1,2,3,4]
2、对象实现了 __reversed__() 的特殊方法时才能生效

3、如果不符合以上任意一个条件，则需要将其转化成list
    需要注意的是，有的可迭代对象元素很多，预先转换成list会消耗很多内存资源
"""


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


if __name__ == '__main__':
    for rr in reversed(Countdown(30)):
        print(rr)

