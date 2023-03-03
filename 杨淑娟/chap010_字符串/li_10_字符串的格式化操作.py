# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/9 14:20

# 使用 % 作占位符
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))

# 使用 {} 作占位符，配合.format()方法
print('我叫{0}，今年{1}岁'.format(name, age))

# f-string
print(f'我叫{name}，今年{age}岁')
