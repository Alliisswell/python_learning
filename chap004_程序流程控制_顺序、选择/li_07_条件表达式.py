# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/4 13:13
"""
语法：
条件执行体1 if 条件表达式 else 条件执行体2
（即双分支结构if...else的简写形式）
"""
# 比较大小
a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
# （双分支结构）
# if a >= b:
#     print( a, '大于等于', b)
# else:
#     print( a, '小于', b )
# （条件表达式）
print(str(a) + '大于等于' + str(b) if a >= b else str(a) + '小于' + str(b))
