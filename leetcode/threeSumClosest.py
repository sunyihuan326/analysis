# coding:utf-8 
'''
created on 2019/1/17

@author:sunyihuan
'''


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = sum((nums[i], nums[l], nums[r]))
            if abs(s - target) < abs(res - target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:  # break early
                return res
    return res


print(threeSumClosest([0, 2, 1, -3], 1))
