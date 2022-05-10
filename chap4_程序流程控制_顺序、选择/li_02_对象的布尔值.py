# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/4 10:41
"""
Python一切皆对象，所有对象都有一个布尔值
    获取对象的布尔值，使用内置函数bool()

以下对象的布尔值为False
    False
    数值0或0.0
    None
    空字符串
    空列表
    空元组
    空字典
    空集合

其他所有对象的布尔值均为True
"""
print( bool( False ) )
print( bool(0) )
print( bool(None) )
print( bool('') )
print( bool("") )
# 空列表
print( bool([]) )
print( bool(list()) )
# 空元组
print( bool(()) )
print( bool(tuple()) )
# 空字典
print( bool({}) )
print( bool(dict()) )
# 空集合
print( bool(set()) )


