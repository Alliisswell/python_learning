# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/7 19:38

t = (98, 'python', 12.3, 98)

print( t[0] )
print( t[1] )
print( t[2] )

print(t.__getitem__(0))
print(t.__getitem__(1))
print(t.__getitem__(2))

# 元组的常见操作
print(t.index(12.3))  # 求元素的索引下标
print(t.count(98))  # 统计某个相同元素个数
print(len(t))  # 求元组元素个数

