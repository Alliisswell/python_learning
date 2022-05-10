# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/4 10:54
"""
语法：
if 条件表达式:
    条件执行体
"""
money = 1000
take = int( input( '请输入取款金额：' ) )
if money >= take:
    money -= take
    print( '余额为：', money )
