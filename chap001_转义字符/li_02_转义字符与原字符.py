# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/1 21:11

# 转义字符
print('hello\nworld')  # 换行  n-->newline
print('hello\tworld')  # 一个制表位占四个空格
print('hello123\tworld')
print('hello\rworld')  # 回车  r-->return
print('hello\bworld')  # 退回一格
print('http:\\www.baidu.com')
print('老师说：\"大家好\"')  # 输出英文输入法状态下的双引号
print('老师说：\'大家好\'')  # 输出英文输入法状态下的单引号

# 原字符，不希望字符串中的转义字符起作用，就是在字符串前边加上r或者R
print(r'1hello\nworld')
print(R'2hello\nworld')
# 注意事项：在使用原字符时，最后一个字符不能是单独一个反斜杠
# print(r'3hello\nworld\')
print(r'4hello\nworld\\')  # 但可以是两个反斜杠

