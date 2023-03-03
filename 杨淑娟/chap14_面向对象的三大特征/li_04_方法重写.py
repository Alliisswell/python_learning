# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/24 10:32
# 分隔工具：print( '*' * 5, '', '*' * 5 )
"""
方法重写：
如果子类对继承自父类的某个方法不满意，可以在子类中对其进行重新编写
子类重写的方法中可以通过 super().**() 调用父类中被重写的方法

"""


# 定义父类：人类
class Person:  # 默认继承Object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'姓名：{self.name}，年龄：{self.age}岁')


# 定义子类一：学生类
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)  # 和 super(Student, self).__init__(name,age) 效果一样
        self.score = score

    def info(self):
        print(f'分数：{self.score}')


# 定义子类二：老师类
class Teacher(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def info(self):
        super().info()  # 使用 super().**() 调用父类中被重写的方法
        print(f'编号：{self.id}')


stu = Student('张三', 20, 90)
tea = Teacher('李老师', 30, 1001)
stu.info()  # 调用重写后的.info()，重写的方法中没有使用 super().**() 调用父类中被重写的方法
tea.info()  # 调用重写后的.info()，重写的方法中使用 super().**() 调用父类中被重写的方法
