# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/3 14:01

# 比较运算符返回的结果是bool类型
a, b = 10, 20
print("a>b?", a > b)
print('a<b?', a < b)
print("a>=b?", a >= b)
print('a<=b?', a <= b)
print("a==b?", a == b)
print('a!=b?', a != b)

print('-----------------------')
'''
一个变量由三部分组成：标识(id)，类型(type)，值(value)
== 比较的是值
如果想比较标识(id)，使用is或is not
'''
c = 10
d = 10
print(c == d)
print(c is d)
print(id(c))
print(id(d))
print(c is not d)


print('------------')
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
print(l1 == l2)
print(l1 is l2)  # list是可变对象
print(id(l1))
print(id(l2))
print(l1 is not l2)
