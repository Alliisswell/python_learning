# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/5 17:08

# else除了与if配合使用，也可以与while循环和for-in循环配合使用
# for-in循环
# for i in range( 3 ):
#     word = input( '请输入密码：' )
#     if word == '123':
#         print( '密码正确' )
#         break
#     else:
#         print( '密码不正确' )
# else:  # 循环体执行完毕，如果当中没有执行break（即循环正常结束），就会接着执行和for搭配的else语句,如果执行了break，则不会再执行和for搭配的else语句
#     print( '密码已锁定' )

# while循环
a = 0
while a < 3:
    word = input('请输入密码：')
    if word == '123':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a += 1
else:  # 循环体执行完毕，如果当中没有执行break（即循环正常结束），就会接着执行和while搭配的else语句，如果执行了break，则不会再执行和while搭配的else语句
    print('密码已锁定')
