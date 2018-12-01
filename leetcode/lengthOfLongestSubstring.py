# coding:utf-8 
'''
created on 2018/11/20

@author:sunyihuan
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best_str = ""
        max_ = 0

        for s_c in s:
            if s_c not in best_str:
                best_str = best_str + s_c
            else:
                max_ = max(max_, len(best_str))
                temp = best_str[best_str.find(s_c) + 1:len(best_str)] + s_c
                best_str = temp
        return max(max_, len(best_str))


best_str = "abc"
s_c = "c"
print(best_str[best_str.find(s_c) + 1:len(best_str)])
temp = best_str[best_str.find(s_c) + 1:len(best_str)] + s_c

print(temp)
