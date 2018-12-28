# coding:utf-8 
'''
created on 2018/12/4

@author:sunyihuan
'''
l = "efeedee"


# print(l.find("s"))
# print(l.count("s"))


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    size = len(s)
    if size == 1:
        return s
    if size == 2:
        if s[0] == s[1]:
            return s
        return s[0]
    maxp = 1
    ans = s[0]
    i = 0
    while i < size:
        j = i + 1
        while j < size:
            if s[i] == s[j]:
                j += 1  # 判断相邻两数字是否相等
            else:
                break
        k = 0  # 以i为中心向左的步长
        while i - k - 1 >= 0 and j + k <= size - 1:
            if s[i - k - 1] != s[j + k]:      #非回文暂停
                break
            k += 1
        if j - i + 2 * k > maxp:
            maxp = j - i + 2 * k
            ans = s[i - k:j + k]
        if j + k == size - 1:
            break
        i = j
    return ans


# print(longestPalindrome(l))

def longestPalindrome0(s):
    lens = len(s)
    if lens < 2:
        return s
    maxlen = 0
    start = 0
    for i in range(lens):
        for j in range(i):
            begin = j
            end = i
            while begin < end:
                if s[begin] != s[end]:
                    break
                begin += 1
                end -= 1
            if begin >= end and i - j + 1 > maxlen:
                maxlen = i - j + 1
                start = j
    if maxlen > 0:
        return s[start:start + maxlen]


print(longestPalindrome(l))
