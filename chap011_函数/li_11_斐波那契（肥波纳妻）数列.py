# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/10 17:27
# 分隔工具：print('*' * 5, '', '*' * 5)

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        res = fib( n - 2 ) + fib( n - 1 )
        return res


print( fib( 6 ) )

print('*' * 5, '计算输出斐波那契数列前六项的和', '*' * 5)
res2 = 0
for i in range( 1, 7 ):
    print(fib(i))
    res2 = res2 + fib( i )

print(res2)