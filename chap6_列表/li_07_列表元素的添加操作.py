# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 11:36

# 在列表末尾添加一个元素（常用操作）
lst = [10, 20, 30]
print( '添加元素之前', lst, id( lst ) )
lst.append( 100 )
print( '添加元素之后', lst, id( lst ) )

# 在列表末尾至少添加一个元素
lst2 = ['hello', 'world']
lst.append( lst2 )  # 将lst2整体作为一个元素添加至末尾
print( lst )

lst3 = ['hello', 'world']
lst.extend( lst3 )  # 将lst3内的多个元素一次性依次添加至末尾
print( lst )

# 在任意位置上添加一个元素
lst.insert( 1, 90 )
print( lst )


