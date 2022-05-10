# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/5 21:22

for i in range( 5 ):
    for j in range( 1, 11 ):
        if j % 2 == 0:
            break
        print( j )

for i1 in range( 5 ):
    for j1 in range( 1, 11 ):
        if j1 % 2 == 0:
            continue
        print( j1, end='\t' )
    print()
