# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/9 14:18

# .replace()方法
# 第一个参数指定被替换的子串，第二个参数指定替换的子串
# 该方法返回替换后得到的新字符串，替换前的字符串不发生变化
# 第三个参数指定最大替换次数

s = 'hello world hello python'
print( s, id( s ) )
lst = s.replace( 'hello', 'goodbye' )
print( lst, id( lst ) )
print( s, id( s ) )

print( '指定最大替换次数' )
s1 = 'hello world hello python'
print( s1, id( s1 ) )
lst = s1.replace( 'hello', 'goodbye', 1 )
print( lst, id( lst ) )
print( s1, id( s1 ) )

# .join()方法，将列表或元组中的多个字符串合并成一个字符串
lst = ['hello', 'java', 'python']
print( '|'.join( lst ) )
print( ''.join( lst ) )

lst1 = ('hello', 'java', 'python')
print( '|'.join( lst1 ) )
print( ''.join( lst1 ) )

print( '*'.join( 'python' ) )  # 这里先把字符串变成了可迭代的字符串序列
