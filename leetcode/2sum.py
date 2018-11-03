# coding:utf-8 
'''
created on 2018/11/2

@author:sunyihuan
'''


#
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     import numpy as np
#     x = np.reshape(nums, (len(nums), 1))
#     y = x + nums
#
#     result = np.array(np.where(y == target)).T
#
#     return sorted(result[1])

def twoSum(nums, target):
    hashTable = {}
    for i in range(len(nums)):

        subtract_value = target - nums[i]

        if subtract_value in hashTable:
            return [hashTable[subtract_value], i]

        hashTable[nums[i]] = i


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addtwonumber(l1, l2):
    l1_temp, l2_temp = l1, l2
    final_l = ListNode(None)
    final = final_l
    l1_str, l2_str = "", ""
    while l1_temp is not None:
        l1_str = str(l1_temp.val) + l1_str
        l1_temp = l1_temp.next

    while l2_temp is not None:
        l2_str = str(l2_temp.val) + l2_str
        l2_temp = l2_temp.next

    res = int(l1_str) + int(l2_str)
    res = str(res)

    for i in range(1, len(res) + 1):
        temp_node = ListNode(int(res[-i]))
        final_l.next = temp_node
        final_l = final_l.next
    final = final.next
    return final


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1 / x
    if n % 2 == 0:
        return myPow(x * x, int(n / 2))
    else:
        return x * myPow(x * x, int(n / 2))


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    s = []
    for i in range(0, len(str) - 1):
        if str[i] != " ":
            if str[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]:
                return 0


l1 = [3, 3, 4]
l2 = [3, 8, 4]
# print(addtwonumber(l1, l2))
print(myPow(3.2, -3))
