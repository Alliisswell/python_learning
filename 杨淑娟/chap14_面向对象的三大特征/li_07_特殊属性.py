# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/24 16:10
# 分隔工具：print( '*' * 5, '', '*' * 5 )

# 特殊属性：__属性__
print(dir(object))


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('我是C类')


class D(A):
    pass


x = C('C1', 20)

print(x.__dict__)  # __dict__ 获得类对象所绑定的所有属性、方法或实例对象所绑定的所有属性的字典
print(C.__dict__)
print('*' * 5, '', '*' * 5)
print(x.__class__)  # 输出对象所属的类
print(C.__bases__)  # 输出一个元组，元素是所有父类
print(C.__base__)  # 输出第一个父类
print(C.__mro__)  # 查看类的层次结构
print(A.__subclasses__())  # 输出一个列表，元素是所有子类
