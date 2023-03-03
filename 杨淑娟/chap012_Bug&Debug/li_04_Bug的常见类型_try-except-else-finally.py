# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/17 20:30
# 分隔工具：print('*' * 5, '', '*' * 5)

# try...except...else...finally结构
# 无论是否发生过异常，finally块都会被执行，常用来释放try块中申请的资源

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as err:
    print('出错了！')
    print(err)
else:
    print('结果为：', result)
finally:
    print('谢谢您的使用！')
print('程序结束！')
