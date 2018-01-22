# coding:utf-8
'''
Created on 2017/2/20

@author: sunyihuan
'''


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def preTraverse(root):
        if root == None:
            return
        print(root.value)
