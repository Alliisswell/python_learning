# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/6 11:37

# 通过调用列表对象的sort方法，默认升序排序
lst = [30, 50, 20, 60, 10, 40]
print( '排序前', lst, id( lst ) )
lst.sort()
print( '排序后', lst, id( lst ) )
# 指定关键字，进行降序排序
lst.sort( reverse=True )
print( lst )

print( '-----------使用内置函数sorted()对列表排序，将产生一个新列表---------' )
lst2 = [30, 50, 20, 60, 10, 40]
print( '排序前：', lst2, id( lst2 ) )
new_list = sorted( lst2, reverse=True )
print( '排序后：', new_list, id( new_list ) )
