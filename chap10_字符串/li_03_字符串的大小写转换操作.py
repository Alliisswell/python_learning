# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/9 11:43

# .upper()方法，把字符串中所有字符转换成大写字母
s = 'hEllo,woRld'
a = s.upper()  # 转换之后产生一个新的字符串
print( a, id( a ) )
print( s, id( s ) )  # 原来的字符串并没有发生改变

# .lower()方法，把字符串中所有字符转换成小写字母
b = s.lower()  # 转换之后产生一个新的字符串
print( b, id( b ) )
print( s, id( s ) )  # 原来的字符串并没有发生改变

# .swapcase()方法，把字符串中所有字母大小写互换
d = s.swapcase()  # 转换之后产生一个新的字符串
print( d, id( d ) )
print( s, id( s ) )  # 原来的字符串并没有发生改变

# .capitalize()方法，把第一个字符转换为大写，把其余字符都转换成小写
e = s.capitalize()  # 转换之后产生一个新的字符串
print( e, id( e ) )
print( s, id( s ) )  # 原来的字符串并没有发生改变

# .title()方法，把每个单词的第一个字符转换成大写，把每个单词的其余字符都转换成小写
f = s.title()
print( f, id( f ) )
