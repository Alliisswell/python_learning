# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/21 16:29
# 分隔工具：print('*' * 5, '', '*' * 5)

class Student1:  # 类名由一个或多个单词组成，每个单词的首字母需要大写，其余小写
    pass


# Python中一切皆对象，类也是一个对象，叫做类对象（类的对象就叫做实例对象）
print(Student1)
print(id(Student1))
print(type(Student1))


class Student2:
    native_pace = '吉林'  # 直接写在类里的变量，称为属性

    # 初始化方法
    def __init__(self, name, age):  # name,age为实例属性
        self.name = name  # 将局部变量name的值赋给实例属性self.name（这个.nam可以是其他名称，但是一般习惯上和传入的形参名一样）
        self.age = age

    # 实例方法
    def eat(self):  # 有默认参数self
        print('学生在吃饭')

    # 静态方法
    @staticmethod
    def sm():  # 无默认参数
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):  # 有默认参数cls
        print('我使用了classmethod进行修饰，所以我是类方法')


# 在类外定义的称为函数，再类内定义的称为方法
def drink():
    print('喝水')
