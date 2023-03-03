# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/8 14:33
# 分隔工具：print( '*' * 5, '', '*' * 5 )
"""
with语句可以自动管理上下文资源，不论是什么原因跳出with块，都能确保文件的关闭，以此来达到释放资源的目的
"""

# 1 举例
# with open( 'a.txt', 'r', encoding='utf-8' ) as file:
#     print( file.read() )


# 2 原理
"""
类 MyContentMgr 实现了特殊方法__enter__(),__exit__()称为该类对象左手了上下文管理器协议
该类对象的实例对象 MyContentMgr() ，称为上下文管理器
"""
# class MyContentMgr:
#     def __enter__(self):
#         print( 'enter方法被调用了' )
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print( 'exit方法被调用了' )
#
#     def show(self):
#         print( 'show方法别调用了' )
#
#
# with MyContentMgr() as file:  # 相当于 file = MyContentMgr()
#     file.show()


# 3 举例
with open('logo.png', 'rb') as src_file:
    with open('copylogo2.png', 'wb') as target_file:
        target_file.write(src_file.read())
