# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/10 17:08
# 分隔工具：print('*' * 5, '', '*' * 5)

# 局部变量：在函数体内部定义并且使用的变量，只有在函数内部有效；局部变量使用global声明，就会变成全局变量
def fun(a, b):
    c = a + b
    print(c)


fun(10, 20)


def fun3():
    global a
    a = 3000
    print(a)


fun3()

# 全局变量：函数体外部定义的变量，可作用于函数体内部
name = '张三'


def fun2():
    print(name)


fun2()
