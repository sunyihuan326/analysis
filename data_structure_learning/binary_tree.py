# coding:utf-8 
'''
created on 2018/10/31

@author:sunyihuan
'''


class Node():

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right


def pro_order(tree):  # 先序遍历
    if tree == None:
        return False
    print(tree._data)
    pro_order(tree._left)
    pro_order(tree._right)


def pos_order(tree):  # 后序遍历
    if tree == None:
        return False
    # print(tree.get_data())
    pos_order(tree._left)
    pos_order(tree._right)
    print(tree._data)


def mid_order(tree):  # 中序遍历
    if tree == None:
        return False
    # print(tree.get_data())
    mid_order(tree._left)
    print(tree._data)
    mid_order(tree._right)


def row_order(tree):  # 层次遍历
    # print(tree._data)
    queue = []
    queue.append(tree)
    while True:
        if queue == []:
            break
        print(queue[0]._data)
        first_tree = queue[0]
        if first_tree._left != None:
            queue.append(first_tree._left)
        if first_tree._right != None:
            queue.append(first_tree._right)
        queue.remove(first_tree)


if __name__ == '__main__':
    tree = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))
    # pro_order(tree)
    # mid_order(tree)
    # pos_order(tree)
    row_order(tree)
