# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/4 11:10
total = int(input('总金额：'))
answer = input('您是会员吗？y/n ')
if answer == 'y':
    print('尊贵的会员您好！')
    if total >= 200:
        print('打八折，付款金额为：', total * 0.8)
    elif total >= 100:
        print('打九折，付款金额为：', total * 0.9)
    else:
        print('不打折，付款金额为：', total)
else:
    print('您不是会员！不打折，付款金额为：', total)
