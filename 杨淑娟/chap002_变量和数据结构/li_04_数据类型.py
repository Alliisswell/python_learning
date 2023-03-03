# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/2 15:54
"""
数据类型：
整数类型-->int(integer)
浮点数类型-->float
布尔类型-->bool(boolean)
字符串类型-->str(string)
"""
# 整数类型
# 可以表示，正数，负数，0
n1 = 98
n2 = -98
n3 = 0
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
# 可以表示成二进制，八进制，十进制，十六进制
print('十进制', 180)  # 默认是十进制
print('二进制', 0b10101111)  # 二进制以0b开头，b不区分大小写
print('八进制', 0o176)  # 八进制以0o开头，o不区分大小写,但是最好用小写，以免和零混淆
print('十六进制', 0x1EAF)  # 十六进制以0x开头，x不区分大小写

print('-' * 30)
# 浮点数类型
# 注意事项：使用浮点数进行计算时，可能会出现小数位数不确定的情况
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1 + n2)  # 3.3000000000000003
print(n1 + n3)  # 3.2
# 解决方案：导入decimal模块
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))  # 3.3

print('-' * 30)
# 布尔类型（与c++的不同点：可以转化为整数并进行计算）
b1 = True
b2 = False
print(b1)
print(b1 + 1, type(b1))  # 2
print(b2)
print(b2 + 1, type(b2))  # 1

print('-' * 30)
# 字符串类型
# 返回值是迭代器对象
# 可以使用单引号，双引号，三单引号或三双引号来定义
# 单双引号定义的字符串必须一行
# 三引号定义的字符串可以分布在连续的多行
str1 = '人生苦短，我用Python'
str2 = "人生苦短，我用Python"
str3 = '''人生苦短，
我用Python'''
str4 = """人生苦短，
我用Python"""
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))
