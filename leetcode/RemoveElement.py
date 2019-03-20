# coding:utf-8 
'''
created on 2019/3/20

@author:sunyihuan
'''


class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
