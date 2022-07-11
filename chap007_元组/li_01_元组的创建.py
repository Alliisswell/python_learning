# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/7 16:39

# 元组tuple
"""
元组与列表的区别：
tuple和list非常类似，但是tuple一旦初始化就不能修改，因此，没有append()，insert()这样的方法
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
"""

# 使用()
t = ('python', 12.3, 98)
print(t)
print(type(t))
# 小括号可以省略不写
t3 = 'python', 12.3, 98
print(t3)
print(type(t3))

# 只包含一个元组元素时需要使用逗号和小括号
s = 'python'  # 这是字符串的定义方式
# t4 = ('python')  # 警告：小括号冗余，就是说系统认为这是在定义一字符串，而且多加了小括号
# print( t4 )
# print( type( t4 ) )  # <class 'str'>
t5 = ('python',)
print(t5)
print(type(t5))

# 使用内置函数tuple()
t2 = tuple(('python', 12.3, 98))
print(t2)
print(type(t2))

# 空元组
t6 = ()
t7 = tuple()
print(t6)
print(t7)



