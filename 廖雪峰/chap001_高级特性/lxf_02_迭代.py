# -*- coding: utf-8 -*-

def findMinAndMax(l):
    minnum = lst[1]
    maxnum = lst[1]
    for num in l:
        if num < minnum:
            minnum = num
        if num > maxnum:
            maxnum = num

    return minnum, maxnum


lst = [1, 3, 5, 7]
print(findMinAndMax(lst))
