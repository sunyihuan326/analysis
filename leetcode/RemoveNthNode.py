# coding:utf-8 
'''
created on 2019/2/17

@author:sunyihuan
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        head_head = ListNode(1)
        head_head.next = head
        length = 1
        while head.next:
            length += 1
            head = head.next
        remove_node_ind = length - n

        ind = 0
        head = head_head

        while head.next:
            if ind == remove_node_ind:
                head.next = head.next.next
                break
            ind += 1
            head = head.next

        return head_head.next

