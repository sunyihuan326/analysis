# coding:utf-8 
'''
created on 2019/2/17

@author:sunyihuan
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        result = ListNode(0)
        l = result
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            # 融合后链表的下一位,当前位置刚刚赋值
            l = l.next
        # 把剩余的链表排在后面
        l.next = l1 or l2
        # 返回融合后链表从第二个对象开始，第一个对象是自己创建的ListNode(0)
        return result.next


arr1 = [1, 2, 3]
arr2 = [5, 6, 7]
l1 = ListNode(arr1[0])
p1 = l1
l2 = ListNode(arr2[0])
p2 = l2
for i in arr1[1:]:
    p1.next = ListNode(i)
    p1 = p1.next
for i in arr2[1:]:
    p2.next = ListNode(i)
    p2 = p2.next
s = Solution()
# 融合两个链表
q = s.mergeTwoLists(l1, l2)

