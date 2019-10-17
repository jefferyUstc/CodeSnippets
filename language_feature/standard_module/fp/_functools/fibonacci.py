from functools import partial, partialmethod
basetwo = partial(int, base=2)
print(basetwo('11'))

def add(x, y):
    return x +y

add(5,6)
add(5,6)