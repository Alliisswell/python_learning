# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/7 22:14
# 分隔工具：print( '*' * 5, '', '*' * 5 )

"""
安装：在系统终端中在线安装，使用以下命令
    pip install 模块名
导入：安装完成之后，进入python解释器，进行导入操作命令
    import 模块名
"""

import time

import schedule


def job():
    print('哈哈')


schedule.every(3).seconds.do(job)
num = 0
while num < 10:
    schedule.run_pending()
    time.sleep(1)
    num += 1
