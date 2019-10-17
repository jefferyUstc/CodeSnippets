from itertools import product, permutations, combinations, combinations_with_replacement
from scipy.special import comb, perm

# -----------------------product-------------------------
print(list(product([1, 2, 3, 4], [1, 2], repeat=1)))  # *iterables, 他们之间进行笛卡尔积

# -----------------------permutations-------------------------
per = list(permutations([1, 2, 3, 4], r=2))  # 有序
assert len(per) == perm(4, 2)  # A^2_4, 排列组合问题
print(per)

# -----------------------combinations-------------------------

per = list(combinations([1, 2, 3, 4], r=2))  # 无放回抽样
assert len(per) == comb(4, 2)  # C^2_4
print(per)

# -----------------------combinations-------------------------

per = list(combinations_with_replacement([1, 2, 3, 4], r=2))  # 有放回抽样
assert len(per) == comb(4, 2, repetition=True)  # 10
print(per)
