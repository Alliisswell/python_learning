# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/17 20:30
# 分隔工具：print('*' * 5, '', '*' * 5)

# try...except...else结构
# 如果try块中没有抛出出异常，则执行else块，如果try中抛出异常，则执行except块

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as err:
    print('出错了！')
    print(err)
else:
    print('结果为：', result)
