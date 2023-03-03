# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/7 14:02

# 遍历字典,根据键来遍历
# 遍历的是key值
scores = {'张三': 100, '李四': 98, '王五': 45}
for item in scores:
    print(item, scores[item])  # 使用[]获取value
for item in scores:
    print(item, scores.get(item))  # 使用.get()获取value
