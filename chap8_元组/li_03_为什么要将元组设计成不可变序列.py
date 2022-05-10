# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/7 19:56
"""
在多任务环境下，同事操作对象时不需要加锁
在程序中尽量使用不可变序列
元组中存储的是对象的引用，不能更改引用，但是对于可变对象（list,tuple）可以更改该对象的数据
"""

t = (10, [20, 30], 9)
print( t )
print( t[0], type( t[0] ), id( t[0] ) )
print( t[1], type( t[1] ), id( t[1] ) )
print( t[2], type( t[2] ), id( t[2] ) )

"""尝试更改列表指向"""
l2 = [100, 200]
print( l2, id( l2 ) )
# t[1] = l2  # 报错：TypeError: 'tuple' object does not support item assignment
"""由于列表[20,30]是可变序列，所以可以向列表中添加元素，而列表的内存地址不变"""
t[1].extend( l2 )  # 向列表添加元素
print( t, id( t[1] ) )  # 可以看到列表的内存地址没有发生改变
