# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/8 16:07
# 分隔工具：print( '*' * 5, '', '*' * 5 )
import os

path = os.getcwd()
lst_files = os.walk( path )
for dirpath, dirname, filename in lst_files:
    # print( dirpath )
    # print( dirname )
    # print( filename )
    # print( '-----------------' )
    for dir in dirname:
        print( os.path.join( dirpath, dir ) )
    for file in filename:
        print( os.path.join( dirpath, file ) )
    print( '-----------------' )
