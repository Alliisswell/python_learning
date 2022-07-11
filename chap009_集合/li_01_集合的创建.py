# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/8 13:18

# 集合：内置数据类型，没有value的字典，元素排列是无序的，和列表和字典一样都属于可变类型的序列

# 使用{}
s = {2, 3, 4, 4, 5, 5, 6}  # 集合中的元素不允许重复,集合中的元素就是字典中的key，所以是不能重复的。
print(s, type(s))  # {2, 3, 4, 5, 6} <class 'set'> 重复元素会被覆盖掉

# 使用内置函数set()，参数需要是可迭代对象str,range(),list,tuple,dict,set
s1 = set('python')
print(s1, type(s1))

s2 = set(range(6))
print(s2, type(s2))

s3 = set([1, 2, 2, 4, 4, 6])
print(s3, type(s3))

s4 = set((1, 2, 2, 4, 4, 65))
print(s4, type(s4))

s5 = set({34, 34, 5, 6, 76, 76, 4})
print(s5, type(s5))

# 空集合
s7 = {}  # 由于空字典的定义已经使用了该方法，所以空集合的定义只能使用内置函数
print(s7, type(s7))  # {} <class 'dict'>

s8 = set()
print(s8, type(s8))  # set() <class 'set'> 注意这里打印空集合结果是 set() 也是由于 {} 被空字典使用了
