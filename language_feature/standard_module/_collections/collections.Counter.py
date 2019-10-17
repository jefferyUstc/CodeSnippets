from collections import Counter

a = [1, 2, 3, 5, 4, 5, 5, 4, 4, 3, 2, 2, 2, 2, 1]
a = list(map(str, a))
counter = Counter(a)

print(counter)  # 可以当做一个字典处理
"""
Counter({'2': 5, '5': 3, '4': 3, '1': 2, '3': 2})
"""

for key, value in counter.items():
    print('%s: %s' % (key, value))
"""
1: 2
2: 5
3: 2
5: 3
4: 3
"""

counter_pairs = sorted(counter.items(), key=lambda x: -x[1])  # 从大到小排序
print(counter_pairs)
"""type==list
[('2', 5), ('5', 3), ('4', 3), ('1', 2), ('3', 2)]
"""

words, counts = zip(*counter_pairs)
print(words)
print(counts)
"""
('2', '5', '4', '1', '3')
(5, 3, 3, 2, 2)
"""

