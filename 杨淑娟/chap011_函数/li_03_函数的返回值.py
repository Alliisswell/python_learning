# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/10 11:49
# 分隔工具：print('*' * 5, '', '*' * 5)

# 函数返回值有多个时，返回结果为元组

def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


result = fun([10, 29, 34, 23, 44, 53, 55])
print(result, type(result))

"""
总结：
1、函数没有返回值，return可以省略不写
2、函数有一个返回值，直接返回原值（保持原数据类型不变）
3、函数有两个以上函数值，返回结果为元组类型
"""
