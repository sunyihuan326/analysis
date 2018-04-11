# coding:utf-8 
'''
created on 2018/4/3

@author:sunyihuan
'''

import sys

sys.setrecursionlimit(100000000)


def trailingZeros(self, n):
    # write your code here, try to do it without arithmetic operators.
    c = 0
    tem = int(n / 5)
    # print(tem)
    while tem != 0:
        c = c + tem
        # print(c)
        tem = int(tem / 5)
    return c


# print(trailingZeros(self=0, n=5))

def digitCounts(self, k, n):
    # write your code here
    c = 0
    for i in range(n + 1):
        # print(i)
        for j in range(len(str(i))):
            if str(k) == str(i)[j]:
                # print(str(i))
                c = c + 1
    return c


# print(digitCounts(self=0, k=1, n=12))

def nthUglyNumber(self, n):
    # write your code here
    s = []
    u_num = 0
    num = 0
    if n <= 0:
        return ""
    elif n == 1:
        num = 1
    else:
        while u_num < n - 1:
            # print(u_num)
            num += 1
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
                u_num += 1
                # print(num)
                s.append(num)
    return num, s


#
# n, s = nthUglyNumber(self=0, n=41)
# print(n)
# print(len(s))
# print(s)
def findMaxAverage(self, nums, k):
    sum = 0
    for i in range(len(nums)):
        for j in range(len(nums) - i):
            if nums[len(nums) - 1 - j] > nums[i]:
                nums[i], nums[len(nums) - 1 - j] = nums[len(nums) - 1 - j], nums[i]

    for ki in range(k):
        sum = sum + nums[ki]

    return float(sum / k), nums


print(findMaxAverage(self=0, nums=[1, 0, 2, 666666, 3, 68, 7, 90, 8], k=3))
