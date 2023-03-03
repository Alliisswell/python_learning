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
print('1', bool(False))
print('2', bool(0))
print('3', bool(None))
print('4', bool(''))
print('5', bool(""))
print('6', bool(''''''))
print('7', bool(""""""))
# 空列表
print('8', bool([]))
print('9', bool(list()))
# 空元组
print('10', bool(()))
print('11', bool(tuple()))
# 空字典
print('12', bool({}))
print('13', bool(dict()))
# 空集合
print('14', bool(set()))
