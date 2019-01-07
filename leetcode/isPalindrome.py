# coding:utf-8 
'''
created on 2019/1/7

@author:sunyihuan
'''


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    x_reverse = x[::-1]
    if x == x_reverse:
        re = True
    else:
        re = False
    return re


print(isPalindrome(12321))
