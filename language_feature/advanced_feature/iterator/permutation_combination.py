from itertools import permutations, combinations, combinations_with_replacement

items = ['a', 'b', 'c', 'a']

for p in permutations(items):
    """
    给出所有排列组合
    """
    print(p)
print('***')
for p in combinations(items, r=2):
    """
    给出所有组合
    """
    print(p)
print('***')
for p in combinations_with_replacement(items, r=2):
    """
    有放回的给出所有组合
    """
    print(p)
