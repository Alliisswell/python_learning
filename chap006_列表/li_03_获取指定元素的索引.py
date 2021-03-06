# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 10:16

# 获取指定元素的索引
# index（value, start, stop）
# 索引范围：[start, stop)===[start, stop-1]
lst = [98, 'hello', True, 98, 'python', False]
print(lst.index(98))
# print( lst.index( 'world' ) )  # ValueError: 'world' is not in list
# print( lst.index( 98, 1, 3 ) )  # ValueError: 98 is not in list 因为[1,3)===[1,2]
print(lst.index(98, 0, 2))
print(lst.index(98, 3, 5))
print(lst.index(98, 0, 5))  # 如果有重复元素，则能只获得第一个元素的索引

print(lst.count(98))  # 计算元素个数
print(len(lst))  # 计算列表长度
