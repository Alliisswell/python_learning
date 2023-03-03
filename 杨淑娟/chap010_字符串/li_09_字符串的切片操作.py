# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/9 14:19

# 切片的结果是一个新的字符串

s = 'hello,python'
s1 = s[:5]  # 没有指定起始位置，则从0开始
s2 = s[6:]  # 没有指定结束位置，则一直到最后
s3 = '!'
s4 = s1 + s3 + s2
print(s1, id(s1))
print(s2, id(s2))
print(s3, id(s3))
print(s4, id(s4))

print(s[1:5:1])
print(s[::2])
print(s[::-1])
print(s[-6::])
