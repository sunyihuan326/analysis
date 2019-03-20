# coding:utf-8 
'''
created on 2019/3/20

@author:sunyihuan
'''


class Solution:
    def strStr(self, haystack, needle):
        n_l = len(needle)
        if n_l == 0:
            return 0
        if len(haystack) - n_l == 0:
            if haystack == needle:
                return 0
            else:
                return -1
        else:
            for i in range(len(haystack) - n_l + 1):
                if haystack[i:i + n_l] == needle:
                    return i
                    break
        return -1


s = Solution()
print(s.strStr("mississippi", "pi"))
