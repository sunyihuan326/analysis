# coding:utf-8
'''
Created on 2017/2/20

@author: sunyihuan
'''


def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i + 1]:
                c = bubbleList[i]
                bubbleList[i] = bubbleList[i + 1]
                bubbleList[i + 1] = c
        listLength -= 1
    print bubbleList


if __name__ == '__main__':
    bubbleList = [9, 8, 0, 10, 67, 3, 1]
    bubble(bubbleList)
