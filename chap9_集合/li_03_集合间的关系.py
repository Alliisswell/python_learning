# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/8 15:51

# 判断集合相等 == !=
s = {10, 20, 30, 40}
s2 = {30, 20, 40, 10}
print( s == s2 )
print( s != s2 )

# 判断子集关系  子集.issubset(超集)
s3 = {10, 20, 30, 40}
s4 = {10, 20, 30}
s5 = {10, 20, 90}
print( s4.issubset( s3 ) )
print( s5.issubset( s3 ) )

# 判断超集关系  超集.issuperset(子集)
print( s3.issuperset( s4 ) )
print( s3.issuperset( s5 ) )

# 判断是否没有交集 .isdisjoint()
print( s3.isdisjoint( s4 ) )  # False，是有交集的
s5 = {100, 200, 300}
print( s3.isdisjoint( s5 ) )  # True，确实没有交集
