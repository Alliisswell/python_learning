# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/7 14:02
# 字典的特点
# 1、字典中的所有元素都是一个key-value对，key不允许重复，value允许重复
# 2、元素是无序的
# 3、key必须是不可变对象（目前：int，float，str，bool）
# 4、和列表一样，可以根据需要动态地伸缩
# 5、会浪费较大的内存，是一种使用空间换时间的数据结构

# 1、字典中的所有元素都是一个key-value对，key不允许重复，value允许重复
d1 = {'name': '张三', 'name': '李四'}
print( d1 )  # {'name': '李四'} 虽然没有报错，但是丢失了数据“张三”，所以key不允许重复
d2 = {'name': '张三', 'nike_name': '张三'}
print( d2 )

# 3、key必须是不可变对象（目前：int，float，str，bool）
l1 = [10, 20, 30]  # 可变对象
# d3 = {l1: 100}  # 报错 TypeError: unhashable type: 'list'

