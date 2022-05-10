# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/4 18:27
"""
range函数用于生成一个整数序列

返回值是一个迭代器对象

优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，
    因为仅仅需要存储start，stop，step，只有当用到range对象时，才会计算序列中的相关元素
"""
# range( start, stop, step)函数的三种调用方式
# 第一种，只有一个参数，默认从0开始，默认步长为1
r1 = range( 10 )
print( list( r1 ) )
# 第二种，两个参数，默认步长为1
# 第二种，两个参数，默认步长为1
r2 = range( 1, 10 )
print( list( r2 ) )
# 第三种，三个参数
r3 = range( 1, 10, 2 )
print( list( r3 ) )
print( 10 in r3 )
print( 9 in r3 )
print( 10 not in r3 )
print( 9 not in r3 )

print( range( 1, 20 ) )  # [1,,,19]
print( range( 1, 101 ) )  # [1,,,100]
