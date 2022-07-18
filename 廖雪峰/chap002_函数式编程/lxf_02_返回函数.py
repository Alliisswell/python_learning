# 闭包的练习
def createcounter():
    x = 0

    def counter():
        # 函数内部加一个nonlocal x的声明。加上这个声明后，解释器把x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1
        nonlocal x
        x = x + 1
        return x

    return counter


# 测试
counterA = createcounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createcounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
