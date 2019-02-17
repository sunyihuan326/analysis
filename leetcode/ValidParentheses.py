# coding:utf-8 
'''
created on 2019/2/16

@author:sunyihuan
'''


class Solution:
    def match0(self, s1, s2):
        if s1 == '(' and s2 == ')':
            return True

        if s1 == '[' and s2 == ']':
            return True

        if s1 == '{' and s2 == '}':
            return True

        return False

    def isValid(self, s):
        ans = []

        for i in s:
            print(i)
            if i == '(' or i == '{' or i == '[':
                ans.append(i)
            if i == ')' or i == ']' or i == '}':
                if len(ans) == 0:
                    return False
                tmp = ans.pop()
                print(tmp)
                if not self.match0(tmp, i):
                    return False
        if len(ans) == 0:
            return True

        return False

s = Solution()

print(s.isValid("()]"))
