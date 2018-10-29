# coding:utf-8 
'''
created on 2018/10/29

@author:sunyihuan
'''


def BubbleSort(ss):
    n = len(ss)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if ss[j] > ss[j + 1]:
                ss[j + 1], ss[j] = ss[j], ss[j + 1]

    return ss


def SelectionSort(ss):
    n = len(ss)
    for i in range(0, n - 1):
        min = i
        for j in range(i + 1, n):
            if ss[j] < ss[min]:
                min = j
        if min != i:
            ss[i], ss[min] = ss[min], ss[i]
    return ss


def InsertionSort(ss):
    n = len(ss)
    for i in range(0, n):
        j = i - 1
        while (j > 0 and ss[j] > ss[i]):
            ss[j], ss[i] = ss[i], ss[j]
    return ss


def InsertionSortDichotomy(ss):
    n = len(ss)
    pass


if __name__ == "__main__":
    ss = [0, 30, 2, 5, 4, 9, 7, 8, 22]
    # print(BubbleSort(ss))
    # print(SelectionSort(ss))
    print(InsertionSort(ss))
