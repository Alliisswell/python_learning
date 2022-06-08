# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/6 20:39
# 分隔工具：print( '*' * 5, '', '*' * 5 )
import sys  # 与Python解释器及其环境操作相关的标准库

print( sys.getsizeof( 100 ) )
print( sys.getsizeof( 123 ) )
print( sys.getsizeof( True ) )
print( sys.getsizeof( False ) )
print( dir( sys ) )
import time  # 提供与时间相关的各种函数的标准库

print( time.time() )  # 输出数值单位是秒
print( time.localtime( time.time() ) )
import os  # 提供了访问操作系统服务功能的标准库
import calendar  # 提供与日期相关的各种函数的标准库
# import urllib  # 用于读取来自网上（服务器）的数据标准库
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())

import json  # 用于使用JSON序列化和反序列化对象
import re  # 用于在字符串中执行正则表达式匹配和替换
import math  # 提供标准算术运算函数的标准库
import decimal  # 用于进行精准控制运算精度、有效位数和四舍五入操作的十进制运算
import logging  # 提供了灵活地记录事件、错误、警告和调试信息等日志信息的功能
