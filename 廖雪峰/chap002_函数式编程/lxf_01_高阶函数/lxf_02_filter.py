# 妙啊！！！利用切片，反向遍历
def is_palindrome(n):
    num = str(n)
    return num == num[::-1]


output = list(filter(is_palindrome, range(1, 201)))
print('1~200内的回数：', output)
