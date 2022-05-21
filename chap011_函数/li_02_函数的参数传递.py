# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/10 10:34
# 分隔工具：print('*' * 5, '', '*' * 5)

# 主要理解形参和实参的区别，以及认识形参的种类

# 位置实参：根据形参对应的位置进行实参传递
def calc(a, b):
    c = a + b
    return c


result = calc( 10, 20 )
print( result )

# 关键字实参：根据形参名称进行实参传递
result1 = calc( b=20, a=20 )  # “参数列表”中，等号左侧的变量名，称为关键字参数
print( result1 )


print( '*' * 5, '函数参数传递的内存分析', '*' * 5 )


def fun(arg1, arg2):
    print( 'arg1:', arg1 )
    print( 'arg2:', arg2 )
    arg1 = 100
    arg2.append( 55 )
    print( 'arg1:', arg1 )
    print( 'arg2:', arg2 )


n1 = 10
n2 = [22, 33, 44]
print( 'n1:', n1 )
print( 'n2:', n2 )
print( '调用函数' )
fun( n1, n2 )
print('函数调用后')
print( 'n1:', n1 )  # int类型不可变，在函数体内的修改不会影响实参的值，类似于值传递
print( 'n2:', n2 )  # list类型可变，在函数体内的修改会影响实参的值，类似于地址传递
