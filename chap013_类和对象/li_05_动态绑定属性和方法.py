# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/22 11:12
# 分隔工具：print( '*' * 5, '', '*' * 5 )

# Python是动态语言，在创建对象之后，可以动态地绑定属性和方法

class Student:
    def __init__(self, name, age):  # 初始化方法
        self.name = name
        self.age = age

    def eat(self):  # 实例方法
        print( self.name + '在吃饭' )


stu1 = Student( '张三', 20 )
stu2 = Student( '李四', 30 )
print( id( stu1 ) )
print( id( stu2 ) )

print( '*' * 5, '为stu2动态绑定属性', '*' * 5 )
stu2.gender = '女'
print( stu1.name, stu1.age )
print( stu2.name, stu2.age, stu2.gender )

print( '*' * 5, '为stu2动态绑定方法', '*' * 5 )


def show():
    print( '定义在类外，称为函数' )


stu2.show = show  # 将函数“赋值”给实例对象之后，就变成了实例对象的方法
stu2.show()
