# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/9 11:25

# .index()和.find()方法查找子串第一次出现的位置
# .rindex()和.rfind()方法查找子串第最后一次出现的位置
#

s = 'hello,hello'
print(s.index('lo'))  # 3
print(s.find('lo'))  # 3
print(s.rindex('lo'))  # 9
print(s.rfind('lo'))  # 9

# .index()和.rindex()方法查找的字符串不存在时，抛出异常
# .find()和.rfind()方法查找的字符串不存在时，返回-1
# print( s.index( 'k' ) )  # ValueError: substring not found
print(s.find('k'))  # -1
# print( s.rindex( 'k' ) )  # ValueError: substring not found
print(s.rfind('k'))  # -1
