# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 11:38

# 语法：[ 列表元素表达式 for 自定义变量 in 可迭代对象]
lst = [i ** 2 for i in range(1, 10)]
lst2 = set(i ** 2 for i in range(1, 10))
print(lst)
print(lst2)

# 注意事项：“列表元素表达式”通常包含“自定义变量”
