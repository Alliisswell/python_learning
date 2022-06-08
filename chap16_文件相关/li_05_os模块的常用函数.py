# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/8 15:04
# 分隔工具：print( '*' * 5, '', '*' * 5 )
"""
os模块是Python内置的与操作系统功能和文件系统相关的模块，
该模块中的语句的执行结果通常与操作系统有关，
在不同的操作系统上运行，得到的结果可能不一样

os模块和os.path模块用于对目录和文件进行操作
"""

import os

# os.system('notepad.exe')
# os.system('calc.exe')
# os.startfile('E:\\ToDesk\\ToDesk.exe')

# 创建目录
# os.mkdir( 'newdir' )
# 创建多级目录
# os.makedirs( 'newdir1\\newdir2\\newdir3' )

# 返回当前的工作目录
print( os.getcwd() )

# 返回指定路径下的文件和目录信息
lst = os.listdir( '..\\chap16_文件相关' )
print( lst )

# 删除目录
# os.rmdir('newdir')
# 删除多级目录
# os.removedirs('newdir1\\newdir2\\newdir3')

# 将path设置为当前工作目录
# os.chdir('F:\\PyCharmFiles\\yangshujuan_python\\chap17_用于举例')
# print( os.getcwd() )