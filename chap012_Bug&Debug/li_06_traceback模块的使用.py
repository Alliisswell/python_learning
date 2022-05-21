# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/21 11:07
# 分隔工具：print('*' * 5, '', '*' * 5)

# 主动打印异常，可用于日志文件

import traceback

try:
    print( '--------------' )
    print( 10 / 0 )
except:
    traceback.print_exc()
