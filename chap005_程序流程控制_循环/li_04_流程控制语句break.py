# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/5 16:08

# break用于结束循环结构，通常与分支结构if一起使用

# 从键盘录入密码，做多录入三次，如果正确就结束循环
# for-in循环
# for i in range( 3 ):
#     word = input( '请输入密码：' )
#     if word == '123':
#         print( '密码正确' )
#         break
#     else:
#         print( '密码不正确' )
#         if i == 2:
#             print( '密码已锁定' )

# while循环
a = 0
while a < 3:
    word = input( '请输入密码：' )
    if word == '123':
        print( '密码正确' )
        break
    else:
        print( '密码不正确' )
        if a == 2:
            print( '密码已锁定' )
    a += 1
