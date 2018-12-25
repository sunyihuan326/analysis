# coding:utf-8 
'''
created on 2018/12/4

@author:sunyihuan
'''
l = "esefdsdddgggscvfaasatfscxsdwew"
print(l.find("s"))
print(l.count("s"))


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    lens = len(s)
    if lens <= 1:
        return s
    maxlen = 0
    maxl = 0
    maxr = 0
    i = 0
    while i < lens:
        if (lens - i) < maxlen // 2:
            break
        j = i
        k = i
        while (k < lens - 1) and (s[k + 1] == s[j]):  # 寻找最大相同字符的子串作为核
            k = k + 1
        i = k + 1  # 跳过同一核中的其他i
        while (j > 0) and (k < lens - 1) and (s[j - 1] == s[k + 1]):
            j = j - 1
            k = k + 1
        if k - j + 1 > maxlen:
            maxlen = k - j + 1
            maxl = j
            maxr = k
    return s[maxl:maxr + 1]


print(longestPalindrome(l))
