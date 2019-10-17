from itertools import dropwhile, islice
"""跳过开头的带#的行"""


with open('/etc/passwd') as f:
    for line in dropwhile(lambda l: l.startswith('#'), f):
        print(line, end='')

# 如果知道要具体哪些行，可以这样做

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
