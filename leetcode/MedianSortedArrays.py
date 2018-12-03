# coding:utf-8 
'''
created on 2018/12/3

@author:sunyihuan
'''


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums = sorted(nums1 + nums2)
    l = len(nums)
    if l % 2 == 0:
        return (nums[int(l // 2)] + nums[int(l // 2) - 1]) / 2
    else:
        return nums[int(l / 2)]


print(findMedianSortedArrays([1, 2], [3, 7, 4]))
