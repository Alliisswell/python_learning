# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 10:18

# 获取列表中多个元素，切片操作
# 语法：列表名[start: stop: step]
# 切片范围：[start, stop)===[start, stop-1]

lst = [0, 10, 20, 30, 40, 50, 60, 70]

print(1)
# 1、切片的结果是原列表片段的拷贝,返回了一个新对象
print('原列表', id(lst))
lst2 = lst[1:7:1]
print('片段', id(lst2))

print(2)
# 2、step默认值为1
print(lst[1: 6])
print(lst[1: 6:])
print(lst[1: 6: 2])  # step=2

print(3)
# 3、start默认值为：0
print(lst[:7: 1])

print(4)
# 4、stop默认值为：元素个数-1
print(lst[0:: 1])

# step为正数，从前往后索引
# 切片的第一个元素默认是列表的第一个元素
# 切片的最后一个元素默认是列表最后一个元素

print(5)
# 5、step为负数，从后往前索引
# 切片的第一个元素默认是列表的最后一个元素
# 切片的最后一个元素默认是列表的第一个元素
# 同样，切片范围：[start, stop)===[start, stop+1]
print(lst[7:: -1])  # start，stop都得为正数，这里想逆序获取列表第一个元素就用默认值（应该为-1，但是运行结果不正确）
print(lst[:0: -1])
print(lst[6: 2: -2])
