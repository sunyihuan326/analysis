# coding:utf-8 
'''
created on 2019/3/19

@author:sunyihuan
'''
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        temp = ListNode(-1)
        head = temp
        while heap:
            smallestNodeVal = heapq.heappop(heap)
            temp.next = ListNode(smallestNodeVal)
            temp = temp.next
        return head.next


