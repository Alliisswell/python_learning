# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 11:36

# #在列表末尾添加一个元素（常用操作）
lst = [10, 20, 30]
print('添加元素之前', lst, id(lst))
lst.append(100)  # 可以是int,float,str,bool
print('添加元素之后', lst, id(lst))  # 调用list的方法返回的是原对象

# #在列表末尾至少添加一个元素
# ##append()方法插入的元素可以是list，tuple.dict,set
lst2 = ['hello', 'world']
lst.append(lst2)  # 将列表lst2整体作为一个元素添加至末尾
print(lst)

tupl = ('hello', 'world')
lst.append(tupl)  # 将元组tupl整体作为一个元素添加至末尾
print(lst)

dic = {'hello': 11, 'world': 22}
lst.append(dic)  # 将字典dic整体作为一个元素添加至末尾
print(lst)

sett = {'hello': 11, 'world': 22}
lst.append(sett)  # 将集合sett整体作为一个元素添加至末尾
print(lst)

# ##extend()方法插入的元素可以是list，tuple.dict,set(不能是：int,float,str,bool)，但是如果是字典，只能将key依次加入列表的末尾
lst3 = ['hello', 'world']
lst.extend(lst3)  # 将lst3内的多个元素一次性依次添加至末尾
print(lst)

# 在任意位置上添加一个元素
# ##insert()方法插入的元素可以是int,float,str,bool,list,tuple,dict,set
lst.insert(1, 98)
print(lst)
