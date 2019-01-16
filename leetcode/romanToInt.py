# coding:utf-8 
'''
created on 2019/1/16

@author:sunyihuan
'''


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    R = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans, pre = 0, 0
    for ss in s:
        now = R[ss]
        if pre < now:
            ans += now - 2 * pre
        else:
            ans += now
        pre = now
    return ans

print(romanToInt("III"))