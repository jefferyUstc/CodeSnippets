"""
队列两端插入或删除元素时间复杂度都是 O(1)
默认是队头出队列、队尾进队列
"""
from collections import deque

q = deque([1, 2, 5], maxlen=5)
q.append(6)
q.append(7)
q.append(8)  # 1被自动pop出去
print(q)  # deque([2, 5, 6, 7, 8], maxlen=5)

# 最重要的一些方法
# q.pop()
# q.popleft()
# q.append(0)
# q.appendleft(0)
# q.clear()
# q.index(0)
# q.count(5)
# q.extend([99])
# q.extendleft([99])
# q.remove(5)

for i in q:  # 执行改循环只是读取数据，不会出队列
    print(i)

print(q)
