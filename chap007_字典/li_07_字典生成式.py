# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/7 14:05

# 语法：{key表达式: value表达式 for key的变量, value的变量 in zip(key的可迭代对象, value的可迭代对象)}
name = ['张三', '李四', '王五']
score = [100, 90, 80, 70]
d = {'我是' + k: v ** 2 for k, v in zip( name, score )}  # 生成字典时，遵循木桶效应，字典内元素个数与可迭代对象元素个数较小的那一个相等
print( d )
