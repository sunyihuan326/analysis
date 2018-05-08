# coding:utf-8 
'''
created on 2018/5/8

@author:sunyihuan
'''


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        p1 = None
        p2 = head
        while (p2 is not None):
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1


s = Solution()
head = ListNode(20, 3)
cur = head
for i in range(1, 10):
    node = ListNode(i)
    cur.next = node
    cur = node
head = s.reverse(head)
while (head != None):
    print(head.val, end=' ')
    head = head.next
