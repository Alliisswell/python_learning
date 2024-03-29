# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/6 19:44
# 分隔工具：print( '*' * 5, '', '*' * 5 )

"""

Python程序1
    包1
        模块A
        模块B
        模块C
    包2
        模块A
        模块D
    包3
        模块B
        模块E

1、包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
2、作用：
    代码规范
    避免模块名冲突
3、包与目录的区别：
    包含__init__.py文件的目录称为包
    目录里通常不包含__init__.py文件
4、包的导入
    import 包名
    import 包名.模块名
    from 包名 import 模块名
    from 包名.模块名 import 函数、变量、类
"""

# 包的导入

# import package1
# 可以这样书写，但是只导入包不能进行索引包内模块，所以就没什么意义

import package1.moduleA as ma  # 这里是导入一个包中的某个模块，书写会很长，可以起别名

print(ma.a)
