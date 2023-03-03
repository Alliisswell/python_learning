# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/6 15:30
# 分隔工具：print( '*' * 5, '', '*' * 5 )

# from 模块名 import 函数、变量、类

from math import pi  # 从模块导入某项内容

print(pi)
print(pow(2, 3))  # 内置的普通方法
# print(math.pow(2,3))  # 报错，因为并没有导入math模块的.pow()方法

from math import pow

print(pow(2, 3))  # 内置的math模块的方法
