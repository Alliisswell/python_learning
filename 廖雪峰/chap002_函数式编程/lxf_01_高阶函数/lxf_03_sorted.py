L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):  # 成绩从高到底
    return -t[1]


L2 = sorted(L, key=by_name)  # 其中，key函数的输入是排序对象的元素
print(L2)

L2 = sorted(L, key=by_score)
print(L2)
