# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/5 20:54

# 打印三行四列的矩形
# for i in range( 0, 3 ):  # 打印行
#     for j in range( 0, 4 ):  # 打印列
#         print( '*', end=' ' )
#     print()
# 使用嵌套循环打印乘法口诀表，使用while和for-in两种循环

row1 =1
while row1<10:  # 打印行
    for column1 in range( 1, row1+1 ):  # 打印列
        print( row1, '*', column1, '=', row1 * column1, end='\t' )
    print()
    row1+=1

