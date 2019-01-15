# coding:utf-8 
'''
created on 2019/1/15

@author:sunyihuan
'''


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxarea = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            maxarea_i = (j - i) * min(height[i], height[j])
            maxarea = max(maxarea_i, maxarea)
    return maxarea


def maxArea0(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l = 0
    r = len(height) - 1
    maxarea = 0
    while l < r:
        maxarea_i = (r - l) * min(height[l], height[r])
        maxarea = max(maxarea_i, maxarea)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maxarea

