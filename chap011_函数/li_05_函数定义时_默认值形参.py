# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/10 14:01
# 分隔工具：print('*' * 5, '', '*' * 5)

# 默认值形参
# 函数定义时，给形参设置默认值，调用函数时，只有当准备传入的实参的值与默认值不同时，才需要将实参传入

def fun(a, b=10, *, c=10, d):  # 位置形参b设置默认值10，关键字形参c设置默认值10
    print( 'a=', a )
    print( 'b=', b )
    print( 'c=', c )
    print( 'd=', d )


fun( 100, d=400 )  # 准备传入的位置实参b和关键字实参的值都为10，与默认参数相同，则不需要再传入b,c
fun( 100, 200, c=300, d=400 )
