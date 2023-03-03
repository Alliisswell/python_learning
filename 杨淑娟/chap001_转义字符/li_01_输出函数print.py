# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/1 16:49

# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('hello world')
print("hello hello")

# 含有运算符的表达式
print(3 + 1)

# 将数据输出到文件中
fp = open('E:\\PycharmProjects\\python_learning-main\\chap001_转义字符\\text.txt', 'a+')  # a+ 的含义：如果不存在则新建文件，如果存在继续追加内容
# 注意文件路径中的 \ 要多加一个 \
# 或者用 / 代替 \\
print('hello world', file=fp)
fp.close()

# 不换行输出
print('hello', 'world', 'python')

# 字符串拼接，用+号
print('hello' + 'world')

# print会默认换行输出
print('输出的内容')  # 等价于 print('输出的内容', end="\n")

# 改变Python换行输出
print('内容', end=" ")
print('内容', end="···")
