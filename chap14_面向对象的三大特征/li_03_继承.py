# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/23 20:42
# 分隔工具：print( '*' * 5, '', '*' * 5 )
"""
继承语法：
class 子类类名（父类1，父类2，...）:
    pass
1、如果一个类没有继承任何类，则默认继承object
2、Python支持多继承（C++也支持多继承）
3、定义子类时，必须在其构造函数中调用父类的构造函数
"""


# 定义父类：人类
class Person:  # 默认继承Object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print( f'姓名：{self.name}，年龄：{self.age}岁' )


# 定义子类一：学生类
class Student( Person ):
    def __init__(self, name, age, score):
        # super(Student, self).__init__(name,age)
        super().__init__( name, age )  # 定义子类时，必须在其构造函数中调用父类的构造函数
        self.score = score


# 定义子类二：老师类
class Teacher( Person ):
    def __init__(self, name, age, id):
        super().__init__( name, age )
        self.id = id


stu = Student( '张三', 20, 90 )
tea = Teacher( '李老师', 30, 1001 )
stu.info()
tea.info()


# 多继承
class A:
    pass


class B:
    pass


class C( A, B ):
    pass
