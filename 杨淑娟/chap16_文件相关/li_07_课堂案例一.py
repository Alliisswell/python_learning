# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/8 16:07
# 分隔工具：print( '*' * 5, '', '*' * 5 )
import os

path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
