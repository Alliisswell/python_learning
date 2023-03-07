# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/21 20:50
# 分隔工具：print('*' * 5, '', '*' * 5)

class Student:
    # 静态属性
    native_pace = '吉林'  # 直接写在类里的变量，称为类的静态属性

    # 初始化方法
    def __init__(self, name, age):  # name,age为实例属性
        self.name = name  # 将局部变量name的值赋给实例属性self.name
        self.age = age

    # 实例方法，不能直接调用，需要先进行实例化
    def eat(self):
        print('学生在吃饭')

    # 静态方法，直接调用，不需要实例化
    @staticmethod
    def sm():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法，直接调用，不需要实例化
    @classmethod
    def cm(cls):
        print('我使用了classmethod进行修饰，所以我是类方法')


# 通过实例访问静态属性
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_pace)
print(stu2.native_pace)
# 通过类修改静态属性
Student.native_pace = '天津'
print(stu1.native_pace)
print(stu2.native_pace)

# 静态方法的调用
print('*' * 5, '调用静态方法', '*' * 5)
Student.sm()

# 类方法的调用
print('*' * 5, '调用类方法', '*' * 5)
Student.cm()
stu1.cm()
