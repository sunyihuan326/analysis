# coding:utf-8 
'''
created on 2019/1/17

@author:sunyihuan
'''


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    nums.sort()
    res = []
    for i, a in enumerate(nums[:-2]):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        d = {}
        for j, b in enumerate(nums[i + 1:]):
            if -a - b in d:
                t = sorted([a, b, -a - b])
                res.append(t)
            else:
                d[b] = 1
    return list(res)


print(threeSum([-1, 0, 1, 2, -1, -4]))
