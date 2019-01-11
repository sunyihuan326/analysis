# coding:utf-8 
'''
created on 2019/1/11

@author:sunyihuan
'''


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
    dp[0][0] = True
    print(dp)
    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            if i >= 2:
                dp[0][i] = dp[0][i - 2]
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
            else:
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]

    return dp[len(s)][len(p)]

print(isMatch("aa","a*"))
