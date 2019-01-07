# coding:utf-8 
'''
created on 2019/1/7

@author:sunyihuan
'''


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= 2 ** 31 or x <= -2 ** 31:
        return 0
    else:
        if x > 0:
            x_ = str(x)
            x_new = x_[::-1]
        else:
            x_ = str(abs(x))
            x_new = x_[::-1]
            x_new = "-" + x_new
        x_new = int(x_new)
        if x_new >= 2 ** 31 or x_new <= -2 ** 31:
            return 0
        else:
            return int(x_new)


print(reverse(1534236469))
