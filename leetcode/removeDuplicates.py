# coding:utf-8 
'''
created on 2019/3/20

@author:sunyihuan
'''


def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    else:
        return len(list(set(nums)))


def removeDuplicates0(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
            i = i - 1
        i = i + 1
    return len(nums)


print(removeDuplicates0([1, 1, 3]))
