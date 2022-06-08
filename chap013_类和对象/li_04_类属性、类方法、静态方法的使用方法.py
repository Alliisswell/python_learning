# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/21 20:50
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


# 类属性的使用方法
# print( Student.native_pace )  # 访问类属性
stu1 = Student( '张三', 20 )
stu2 = Student( '李四', 30 )
print( stu1.native_pace )
print( stu2.native_pace )
Student.native_pace = '天津'
print( stu1.native_pace )
print( stu2.native_pace )
print( '*' * 5, '调用静态方法', '*' * 5 )
Student.sm()
print( '*' * 5, '调用类方法', '*' * 5 )
Student.cm()
