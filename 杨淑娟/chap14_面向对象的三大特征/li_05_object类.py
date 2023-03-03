# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/24 10:58
# 分隔工具：print( '*' * 5, '', '*' * 5 )

"""
object类：
1、object类是所有类的父类，因此所有类都有object类的属性和方法
2、内置函数dir()可以查看指定对象的所有属性
3、object有一个__str__()方法，用于返回一个对于“对象的描述”，
对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，
所以我们经常会对__str__()进行重写
"""


class Student:
    pass


stu = Student()
print(dir(stu))
print(stu)  # 调用默认的__str__()方法，用于返回一个对于“对象的描述” <__main__.Student object at 0x00000183E6318A90>
print(stu.__str__())  # <__main__.Student object at 0x00000183E6318A90>

print('*' * 5, '重写__str__()方法', '*' * 5)


class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'名字：{self.name}，年龄：{self.age}'


stu2 = Student2('张三', 20)
print(dir(stu2))
print(stu2)  # 重写__str__()方法后，这里就会调用重写后的__str__()方法
