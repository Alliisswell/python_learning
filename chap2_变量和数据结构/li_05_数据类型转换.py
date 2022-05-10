# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/3 10:01

name = '张三'
age = 20

print(type(name), type(age))
# print('我叫' + name + '今年' + age + '岁')  # 当颈str类型与int类型进行转换时，报错，解决方案，类型转换
print('我叫' + name + '，今年' + str(age) + '岁')  # 通过str()函数将int类型转换为str类型、
print(type(str(age)))  # 查看转换后的数据类型
print(type(age))

print('-----用str()函数转换其他数据类型-----')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a), str(b), str(c),type(str(a)), type(str(b)), type(str(c)))

# print('-----用int()函数转换其他数据类型-----')
# s1='128'
# s2='76.77'
# s3='hello'
# s4='你好'
# f1=98.7
# b1=True
# print(type(s1),type(s2),type(s3),type(f1),type(b1))
# print(int(s1),type(int(s1)))  # 整数字符串，完美转换
# # print(int(s2),type(int(s2)))  # 小数字符串，不可以
# # print(int(s3),type(int(s3)))  # 字母字符串，不可以
# # print(int(s4),type(int(s4)))  # 汉字字符串，不可以
# print(int(f1),type(int(f1)))  # 浮点型，截取整数部分，舍弃小数部分
# print(int(b1),type(int(b1)))  # 布尔型，完美转换
'''
总结：
转换字符串类型时，只能转化整数字符串
转换浮点型时，会舍弃小数部分
转换布尔型时，完美转换
'''

print('-----用float()函数转换其他数据类型-----')
i=98
s1='128'
s2='76.77'
s3='hello'
s4='你好'
b1=True
print(type(i),type(s1),type(s2),type(s3),type(b1),)
print(float(i),type(float(i)))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
# print(float(s3),type(float(s3)))
# print(float(s4),type(float(s4)))
print(float(b1),type(float(b1)))
'''
总结：
转换整型时，会加.0
转换字符串类型时，整数字符串会加.0，小数字符串完美转换，字母和汉字字符串不可以
转换布尔型时，会加.0
'''
