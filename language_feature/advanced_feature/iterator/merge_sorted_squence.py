import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)


# 合并文件
"""
 特别的，它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测。 
 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完
"""
with open('sorted_file_1', 'rt') as file1, \
        open('sorted_file_2', 'rt') as file2, \
        open('merged_file', 'wt') as outf:
    for line in heapq.merge(file1, file2):
        outf.write(line)
