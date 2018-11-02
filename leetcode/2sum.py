# coding:utf-8 
'''
created on 2018/11/2

@author:sunyihuan
'''


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    import numpy as np
    x = np.reshape(nums, (len(nums), 1))
    y = x + nums

    result = np.array(np.where(y == target)).T

    return sorted(result[1])

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def addtwonumber(l1,l2):
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

print(addtwonumber([2,3,4], [2,4,5]))

