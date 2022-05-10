# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/8 14:27

s = {10, 20, 30, 405, 60}
# 判断
print( 10 in s )
print( 10 not in s )

# 添加元素
# .add()一次添加一个元素
s.add( 80 )
print( s, len( s ) )
# .update()一次添加至少一个元素
s.update( {200, 300, 546} )
print( s, len( s ) )
s.update( [100, 99, 8] )
s.update( (78, 64, 56) )
print( s, len( s ) )
s.update( 'hello' )
print( s, len( s ) )

# 删除元素
# .remove()一次删除一个元素，如果指定元素不存在，报错
s.remove( 8 )
# s.remove(800)  # 报错：KeyError: 800
print( s, len( s ) )
# .discard()一次删除一个元素，如果指定元素不存在，不报错
s.discard( 20 )
s.discard( 20000 )  # 20000不存在，但是未报错
print( s, len( s ) )
# .pop()默认删除排在“第一”的元素，并且只能使用无参的默认形式，不能删除指定元素
s.pop()
print( s, len( s ) )
s.pop()
print( s, len( s ) )
# s.pop(30)  # 不能删除指定元素，报错：TypeError: set.pop() takes no arguments (1 given)
# s.clear()清空集合
s.clear()
print( s, len( s ) )
