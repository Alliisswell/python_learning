# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/8 15:52
# 分隔工具：print( '*' * 5, '', '*' * 5 )

# 路径 = 目录 + 文件名
import os.path

# 获取文件或目录的绝对路径
print( os.path.abspath( 'demo1.py' ) )

# 判断文件或目录是否存在，返回True或False
print( os.path.exists( 'demo1.py' ), os.path.exists( 'demo3.py' ) )

# 将目录与目录或者文件名拼接起来
print( os.path.join( 'F:\\Python', 'li_06_os.path模块的常用函数.py' ) )

# 分离目录和文件名
print( os.path.split( 'F:\\PyCharmFiles\\yangshujuan_python\\chap16_文件相关\\demo1.py' ) )

# 分离文件名和拓展名
print( os.path.splitext( 'demo1.py' ) )

# 从一个路径中提取文件名
print( os.path.basename( 'F:\\PyCharmFiles\\yangshujuan_python\\chap16_文件相关\\demo1.py' ) )

# 从一个路径中提取目录
print( os.path.dirname( 'F:\\PyCharmFiles\\yangshujuan_python\\chap16_文件相关\\demo1.py' ) )

# 用于判断是否为路径
print( os.path.isdir( 'F:\\PyCharmFiles\\yangshujuan_python\\chap16_文件相关\\demo1.py' ),
       os.path.isdir( 'F:\\PyCharmFiles\\yangshujuan_python\\chap16_文件相关' ) )
