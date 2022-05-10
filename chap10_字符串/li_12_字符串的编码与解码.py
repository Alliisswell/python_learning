# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/9 14:20

# 编码：将字符串转换为二进制数据（bytes）
s = '天涯共此时'
print( s.encode( encoding='GBK' ) )  # 在GBK编码格式下，一个汉字占三个字节
print( s.encode( encoding='UTF-8' ) )  # 在UFT-8编码格式下，一个汉字占三个字节

# 解码：将二进制数据转换为字符串
b = s.encode( encoding='GBK' )
print( b.decode( encoding='GBK' ) )
b2 = s.encode( encoding='UTF-8' )
print( b2.decode( encoding='UTF-8' ) )
