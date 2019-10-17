import operator
from itertools import accumulate
from time import time

start = time()
list(accumulate(range(100000000), func=operator.mul))
print('operator:', time()-start)
start = time()
list(accumulate(range(100000000), func=lambda x, y: x*y))
print('lambda', time()-start)
