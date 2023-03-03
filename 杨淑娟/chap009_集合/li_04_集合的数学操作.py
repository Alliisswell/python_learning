# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/8 15:52

# 交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)
print('集合s1', s1)
print('集合s2', s2)

# 并集
print(s1.union(s2))
print(s1 | s2)
print('集合s1', s1)
print('集合s2', s2)

# 差集，需要注意作差的“减数”与“被减数”
print(s1.difference(s2))
print(s1 - s2)
print(s2.difference(s1))
print(s2 - s1)
print('集合s1', s1)
print('集合s2', s2)

# 对称差集，不需要注意作差的“减数”与“被减数”
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s2.symmetric_difference(s1))
print(s2 ^ s1)
print('集合s1', s1)
print('集合s2', s2)
