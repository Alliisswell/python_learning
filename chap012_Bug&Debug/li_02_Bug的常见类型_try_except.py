# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/21 10:54
# 分隔工具：print('*' * 5, '', '*' * 5)

# 被动掉坑：程序代码逻辑没有问题，只是因为用户错误操作或者一些“例外情况”而导致的程序崩溃
# 解决方案：Python提供了异常处理机制，可以在异常出现的时候及时捕获，然后内部“消化”，让程序继续运行

# 多个except结构：捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏可能的异常，可以在最后增加BaseException
# 举例
# 题目要求：输入两个整数并进行除法运算
try:
    a = int( input( '请输入第一个整数：' ) )
    b = int( input( '请输入第二个整数：' ) )
    result = a / b
    print( '计算结果：', result )
except ValueError:
    print('对不起，只能输入数字串')
except ZeroDivisionError:
    print('对不起，除数不允许为零')
except BaseException as err:
    print(err)
