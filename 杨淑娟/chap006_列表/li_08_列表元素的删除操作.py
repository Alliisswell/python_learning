# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 11:36
# 使用按值删除函数remove(value)
lst = [10, 20, 30, 40, 50, 30]
print(lst, id(lst))
lst.remove(30)  # 从列表中移除一个元素，如果有重复元素只移除第一个
print(lst, id(lst))  # 返回原对象
# lst.remove( 100 )  # ValueError: list.remove(x): x not in list

# 使用按位删除函数pop(index)
lst.pop()  # 默认索引，删除列表中最后一个元素
print(lst)
lst.pop(0)
print(lst)
# lst.pop(4)  # IndexError: pop index out of range

# 使用切片
lst[1:2] = []
print(lst)

# 清空
lst.clear()
print(lst)

# 删除
del lst
# print(lst)  # NameError: name 'lst' is not defined
