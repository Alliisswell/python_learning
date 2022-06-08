# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/8 9:54
# 分隔工具：print( '*' * 5, '', '*' * 5 )
"""
读写操作流程：
Python操作文件--->打开或新建文件--->读或写文件--->关闭资源（操作系统的相关资源）

原理：
使用内置函数open()创建文件对象，通过IO流将磁盘文件中的内容与程序中对象映射磁盘上的内容进行同步

语法：
    file = open( filename, mode, encoding )

"""
# r 以只读模式打开文件，文件的指针将会放在文件的开头
file = open( 'a.txt', 'r', encoding='utf-8' )
print( file.readlines() )
file.close()

# w 以只写模式打开文件，
# 如果文件不存在则创建，文件指针在文件开头，
# 如果文件存在则覆盖原有内容，文件指针在文件开头
# file = open( 'b.txt', 'w' )
# file.write('hello world')
# file.close()

# a 以追加模式打开文件，
# 如果文件不存在则创建，文件指针在文件开头，
# 如果文件存在则在文件末尾追加内容，文件指针在原文末尾
# file = open( 'b.txt', 'a' )
# file.write('python')
# file.close()

# b 以二进制模式打开文件，不能单独使用，需要与其它模式一起使用，rb或wb
# src_file = open( 'logo.png', 'rb' )
# target_file = open( 'copylogo.png', 'wb' )
# target_file.write( src_file.read() )
# target_file.close()
# src_file.close()

# + 以读写模式打开，不能单独使用，需要与其它模式一起使用，a+
