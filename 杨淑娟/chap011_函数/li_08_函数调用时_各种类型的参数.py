# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/10 15:39
# 分隔工具：print('*' * 5, '', '*' * 5)
"""位置实参和关键字实参的调用"""


def fun(a, b, *, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


fun(10, 20, c=30, d=40)
fun(a=10, b=20, c=30, d=40)


# fun( 10, 20, 30, 40 )  # 报错：TypeError: fun() takes 2 positional arguments but 4 were given
# 位置形参接收位置形参，也可以接收关键字实参，但是，关键字形参只能接收关键字实参


def fun2(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


# 在函数调用时，将列表中的每个元素依次转换为位置形参传入，需要使用 * 号
lst = [10, 20, 30]
# fun( lst )  # 报错：TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun2(*lst)

# 在函数调用时，将字典中的每个元素依次转换为关键字形参传入，需要使用 ** 号
dic = {'a': 111, 'b': 222, 'c': 333}
# fun(dic)  # 报错：TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun2(**dic)

"""函数定义时，形参的顺序"""


def fun3(a, b, *, c, d, **agrsb):
    pass


def fun4(*agrsa, **agrsb):
    pass


def fun5(a, b=10, *agrsa, c, **agrsb):
    pass
