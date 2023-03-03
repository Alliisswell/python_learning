# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/9 14:17

# .split()方法
# 从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回值是一个列表
# 通过参数sep指定劈分符
# 通过参数maxsplit指定的劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
s = 'hello world python'  # 默认劈分字符是空格，就按照空格进行劈分
print(s.split())

s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))

# .rsplit()方法
# 从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回值是一个列表
# 通过参数sep指定劈分符
# 通过参数maxsplit指定的劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
s2 = 'hello|world|python'
print(s2.rsplit(sep='|', maxsplit=1))
