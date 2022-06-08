# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/21 21:28
# 分隔工具：print('*' * 5, '', '*' * 5)

class Student:
    native_pace = '吉林'  # 直接写在类里的变量，称为属性

    # 初始化方法
    def __init__(self, name, age):  # name,age为实例属性
        self.name = name  # 将局部变量name的值赋给实例属性self.name
        self.age = age

    # 实例方法
    def eat(self):
        print( '学生在吃饭' )

    # 静态方法
    @staticmethod
    def sm():
        print( '我使用了staticmethod进行修饰，所以我是静态方法' )

    # 类方法
    @classmethod
    def cm(cls):
        print( '我使用了classmethod进行修饰，所以我是类方法' )

# 实例化对象，每一个实例对象都有一个指针指向自己的类对象
# 语法：实例名 = 类名()
stu1 = Student( '张三', 20 )
print( stu1 )  # <__main__.Student object at 0x0000020C91B190A0>
print( id( stu1 ) )  # 2253007196320转换为十六进制之后就是0x0000020C91B190A0
print( type( stu1 ) )
print('*' * 5, '', '*' * 5)
print( Student )
print( id( Student ) )
print( type( Student ) )

print('*' * 5, '第一种调用方法的方法', '*' * 5)
stu1.eat()
print(stu1.name)
print(stu1.age)

print('*' * 5, '第二种调用方法的方法', '*' * 5)
Student.eat(stu1)  # 与

