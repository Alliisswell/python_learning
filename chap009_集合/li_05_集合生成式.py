# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/8 15:52

# 集合生成式和列表生成式很接近

set1 = {i * i for i in range(1, 11)}
set2 = set(i * i for i in range(1, 11))
print(set1)
print(set2)
