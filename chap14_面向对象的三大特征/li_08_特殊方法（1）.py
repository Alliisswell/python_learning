# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/24 16:11
# 分隔工具：print( '*' * 5, '', '*' * 5 )

# 特殊方法：__方法__

# __add__
print( '*' * 5, '__add__', '*' * 5 )
a = 20
b = 100
c = a + b  # 两个整数类型对象的相加操作
d = a.__add__( b )
print( c )
print( d )


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)

stu1 = Student( '张大仙' )
stu2 = Student( '李四' )

s1 = stu1 + stu2  # 实现了两个自定义对象的加法运算，因为在自定义类当中编写了 __add__() 特殊方法
print( s1 )
s2 = stu1.__add__( stu2 )
print( s2 )

# __len__
print( '*' * 5, '__len__', '*' * 5 )
lst=[1,2,3,4]
print(len(lst))
print(lst.__len__())
print(len(stu1))


