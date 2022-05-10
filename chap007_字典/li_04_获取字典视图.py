# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/7 14:02

scores = {'张三': 100, '李四': 98, '王五': 45}

# 获取所有key
ks = scores.keys()
print( ks )
print( type( ks ) )  # <class 'dict_keys'> 而非 <class 'str'>
print( list( ks ) )

# 获取所有value
vs = scores.values()  # <class 'dict_values'> 而非 <class 'int'>
print( vs )
print( type( vs ) )
print( list( vs ) )

# 获取所有key-value
kvs = scores.items()
print( kvs )
print( type( kvs ) )
print( list( kvs ) )  # [('张三', 100), ('李四', 98), ('王五', 45)] 转换之后的列表元素是由元组组成的
