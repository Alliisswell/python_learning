# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 11:36

lst = [10, 20, 30, 40, 50, 60, 70]
print(lst, id(lst))

# 一次修改一个值
lst[3] = 100
print(lst, id(lst))  # 返回原对象

# 利用切片，将切下的片段替换成需要添加的内容
# 切除的元素个数一定要大于等于待添加的元素个数
lst3 = [100, False, 'python']
# lst[1:] = lst3  # 大于（stop默认值为：元素个数-1，即从位置1到最后全部切除）
lst[1:7:2] = lst3  # 等于
# lst[1:5:2] = lst3  # 小于，报错ValueError: attempt to assign sequence of size 3 to extended slice of size 2
print(lst)
