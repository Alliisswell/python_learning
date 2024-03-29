# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/24 21:48
# 分隔工具：print( '*' * 5, '', '*' * 5 )

# __new__  用于创建对象
# __init__  对创建的对象进行初始化

class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为：{0}'.format(id(cls)))
        obj = super().__new__(cls)  # 调用父类的__new__()
        print('创建的对象obj的id为：{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))

# 创建Person类的实例对象
p1 = Person('张三', 20)
print('p1这个Person类的实例对象的id为：{0}'.format(id(p1)))
