# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/5 15:26

"""
in表示从可迭代对象中依次取值，又称为遍历（目前的学习内容中，仅字符串和序列是可迭代对象）

for-in遍历的对象必须是可迭代对象
"""

for s in 'hello world':
    print( s, end=' ' )

print()
for r in range( 10 ):
    print( r, end=' ' )

print()
# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为下划线
for _ in range( 5 ):
    print( '认生苦短，我用Python' )

print()
for _ in '12345':
    print( '认生苦短，我用Python' )

print()
# 案例一：计算1到100之间偶数的和，并打印
total = 0
for num in range( 1, 101 ):
    if num % 2 == 0:
        total += num
print( total )

print()
# 案例二：打印100到999之间的水仙花数
for num2 in range( 100, 1000 ):
    ge = num2 % 10
    shi = num2 // 10 % 10
    bai = num2 // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == num2:
        print( num2 )
