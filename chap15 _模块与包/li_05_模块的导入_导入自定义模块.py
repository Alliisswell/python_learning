# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/6 15:43
# 分隔工具：print( '*' * 5, '', '*' * 5 )

# 整体导入
# import calc
# print( calc.add( 10, 20 ) )
# print( calc.div( 10, 20 ) )


# 部分导入
from calc import add  # 这里直接导入会报错，需要右击模块所在目录，将目录标记为 源根

print( add( 10, 20 ) )
