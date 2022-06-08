# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/23 19:57
# 分隔工具：print( '*' * 5, '', '*' * 5 )

class Student:
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄设置为私有属性，属性前边加两个 _

    # 实例方法
    def show(self):
        print( self.name, self.__age )


stu = Student( '张三', 20 )
stu.show()
print( stu.name )
# print(stu.__age)  # 报错：AttributeError: 'Student' object has no attribute '__age' 原因：私有属性，类外不可以直接访问
print(dir(stu))  # 使用内置函数dir()查看对象的属性和方法
print(stu._Student__age)  # 在类外可以通过这样的方式进行访问私有属性


