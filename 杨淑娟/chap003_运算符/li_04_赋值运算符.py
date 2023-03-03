# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/3 12:20

# 赋值运算符，运算顺序：从右往左
i = 3 + 4
print(i)

# 链式复制
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

print('-----参数赋值-----')
c = 20
c += 30
print(c)
c -= 20
print(c)
c *= 10
print(c)
c /= 9
print(c, type(c))
c //= 3
print(c, type(c))
c %= 3
print(c, type(c))

print('-----解包赋值-----')
d1, d2, d3 = 10, 20, 30
print(d1, d2, d3)
# 应用于交换两个变量的值
e1, e2 = 10, 20
print('交换前：', e1, e2)
e1, e2 = e2, e1
print('交换后：', e1, e2)
