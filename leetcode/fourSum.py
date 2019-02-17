# coding:utf-8 
'''
created on 2019/1/22

@author:sunyihuan
'''


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    n = len(nums)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for q in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[q] == target:
                        res.append([nums[i], nums[j], nums[k], nums[q]])
    return res


def fourSum0(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()

    for i, items in enumerate(nums):
        temp_target = target - items
        for x1, items1 in enumerate(nums[i + 1:], i):
            temp_target1 = temp_target - items1
            cache = nums[x1 + 2:]
            start, end = 0, len(cache) - 1
            while start < end:
                if cache[start] + cache[end] == temp_target1:
                    res.append([items, items1, cache[start], cache[end]])
                    start += 1
                    end -= 1
                elif cache[start] + cache[end] > temp_target1:
                    end -= 1
                elif cache[start] + cache[end] < temp_target1:
                    start += 1
    res.sort()
    return res


def fourSum1(nums, target):
    if len(nums) < 4:
        return []
    numlen, res, adict = len(nums), set(), {}
    nums.sort()
    for i in range(numlen):
        for j in range(i + 1, numlen):
            if nums[i] + nums[j] not in adict:
                adict[nums[i] + nums[j]] = [(i, j)]
            else:
                adict[nums[i] + nums[j]].append((i, j))
    for i in range(numlen):
        for j in range(i + 1, numlen - 2):
            digit = target - nums[i] - nums[j]
            if digit in adict:
                for item in adict[digit]:
                    if item[0] > j:
                        res.add((nums[i], nums[j], nums[item[0]], nums[item[1]]))
    return [list(k) for k in res]


print(fourSum1([1, 0, -1, 0, -2, 2], 0))
