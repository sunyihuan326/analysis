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
    for i in range(0, n):
        g = ss[i]
        left = 0
        right = i - 1
        while (left <= right):
            mid = int((left + right) / 2)
            if ss[mid] > g:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, right, -1):
            ss[j + 1] = ss[j]
        ss[right + 1] = g
    return ss


def ShellSort(ss):
    h = 0
    n = len(ss)
    while (h <= n):
        h = int(3 * h + 1)
    while (h >= 1):
        for i in range(h, n):
            j = i - h
            g = ss[i]
            while (j >= 0 and ss[j] > g):
                ss[j + h] = ss[j]
                j = j - h
            ss[j + h] = g
        h = int((h - 1) / 3)
    return ss


def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c


def mergeSort(ss):
    if len(ss) <= 1:
        return ss
    mid = int(len(ss) / 2)
    left = mergeSort(ss[:mid])
    right = mergeSort(ss[mid:])
    return merge(left, right)


def QuickSort(arr, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        divIndex = Partition(arr, firstIndex, lastIndex)

        QuickSort(arr, firstIndex, divIndex)
        QuickSort(arr, divIndex + 1, lastIndex)
        return arr
    else:
        return


def Partition(arr, firstIndex, lastIndex):
    i = firstIndex - 1
    for j in range(firstIndex, lastIndex):
        if arr[j] <= arr[lastIndex]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
    return i


if __name__ == "__main__":
    ss = [0, 30, 2, 5, 4, 9, 7, 8, 22]
    # print(BubbleSort(ss))
    # print(SelectionSort(ss))
    print(QuickSort(ss, 0, len(ss) - 1))
