# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/10 14:17
# 分隔工具：print('*' * 5, '', '*' * 5)
"""
个数可变的关键字参数:
1、定义函数时，可能无法事先确定传递的关键字参数的个数时，使用可变的关键字形参
2、使用 ** 定义个数可变的位置形参
3、返回结果为字典
"""


def fun2(**args):
    print( args )


fun2( a=10 )
fun2( a=10, b=20 )
fun2( a=10, b=20, c=30 )

# 注意事项：
# 1、函数定义时，如果仅定义有个数可变的位置形参，只能定义一个
# def fun3(*args1,*args2):
#     pass


# 2、函数定义时，如果仅定义有个数可变的关键字形参，只能定义一个
# def fun4(**args1,**args2):
#     pass


# 3、函数定义时，如果既有个数可变的位置形参，又有个数可变的关键字形参，那么只能一种一个，并且位置形参在前，关键字形参在后
def fun5(*argsa, **argsb):
    pass


# def fun5(**argsa, *argsb):
#     pass
