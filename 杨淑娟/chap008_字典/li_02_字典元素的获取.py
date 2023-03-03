# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 17:08

# 获取字典元素的value
scores = {'张三': 100, '李四': 98, '王五': 45}

# 使用[]
print(scores['张三'])
# print( scores['陈留'] )  # 使用[]获取字典元素时，不存在的键会报错 KeyError: '陈留'

# 使用.get()方法
print(scores.get('李四'))
print(scores.get('陈留'))  # 使用.get()方法获取字典元素时，不存在的键不会报错，会返None
print(scores.get('麻七', 999))  # 999是自己设置的默认值，当键不存在时，返回我们设置的默认值
