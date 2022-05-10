# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/7 14:01
# 增删改字典元素的value

scores = {'张三': 100, '李四': 98, '王五': 45}
# 判断字典中有无某一个键
print( '张三' in scores )
print( '张三' not in scores )

# 删除指定的键值对
del scores['张三']
print( scores )

# 清空字典所有元素
scores.clear()
print( scores )

# 添加字典元素
scores['陈留'] = 90
print( scores )

# 修改字典元素
scores['陈留'] = 100
print( scores )
