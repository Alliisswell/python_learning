# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/8 11:46
# 分隔工具：print( '*' * 5, '', '*' * 5 )


# file = open( 'a.txt', 'r', encoding='utf-8' )
# # print( file.read( 2 ) )
# # print( file.readline() )
# print( file.readlines() )
# file.close()

# file = open( 'b.txt', 'a' )
# # file.write('\nhello')
# lst = ['\njava', '\npython', '\nc++']
# file.writelines( lst )
# file.close()

# file = open( 'a.txt', 'r', encoding='utf-8' )
# file.seek( 3 )  # utf-8的编码格式下，一个汉字占三个字节
# print( file.read() )
# print( file.tell() )
# file.close()

file = open('c.txt', 'a')
file.write('hello')
file.flush()
file.write('world')
file.close()
# 如果先close后flush会报错
