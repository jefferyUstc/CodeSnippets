from collections import Iterable


def flatten(items,
            ignore_types=(str, bytes)  # 该参数要特别注意
            ):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
            """
            yield from 就会返回所有子例程的值
            也就是说yield from后面加一个Iterable类型的对象即可
            
                def gg():
                    yield from [1, 2, 3, 4]
                    # yield from iter([1, 2, 3, 4])

                for g in gg():
                print(g)
            """
        else:
            yield x


if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items):
        print(x)

