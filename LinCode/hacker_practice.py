# coding:utf-8 
'''
created on 2018/8/16

@author:sunyihuan
'''


def gradingStudents(grades):
    new_grades = []
    for k in range(len(grades)):
        print(grades[k])
        if grades[k] < 38:
            print(1)
            new_grades.append(grades[k])
        else:
            print(2)
            c_5 = grades[k] // 5
            g_ = (c_5 + 1) * 5
            print(g_)
            if g_ - grades[k] < 3:
                print(3)
                new_grades.append(g_)
            else:
                print(4)
                new_grades.append(grades[k])
    return new_grades


# grades = [73, 67, 38, 33]
#
# print(gradingStudents(grades))
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_d = 0
    orange_d = 0
    for i in range(len(apples)):
        if s <= apples[i] + a <= t:
            apple_d = apple_d + 1
    for k in range(len(oranges)):
        if s <= oranges[k] + b <= t:
            orange_d = orange_d + 1
    return apple_d, orange_d


# print(countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]))

def kangaroo(x1, v1, x2, v2):
    print((x2 - x1) / (v1 - v2))
    if (v1 - v2) == 0:
        ans = "NO"
    elif (x2 - x1) / (v1 - v2) < 0 and (x2 - x1) / (v1 - v2) - int((x2 - x1) / (v1 - v2)) != 0:
        ans = "NO"
    else:
        ans = "YES"
    return ans


# print(kangaroo(0, 2, 3, 5))
def getTotalX(a, b):
    count_ = 0
    for i in range(len(a)):
        for k in range(len(b)):
            pass


def missingNumbers(arr, brr):
    a = []
    arr_re = {}
    brr_re = {}
    for l in brr:
        if l not in arr:
            a.append(l)
    for i in set(arr):
        arr_re[i] = arr.count(i)
    for j in set(brr):
        brr_re[j] = brr.count(j)
    for k in arr_re.keys():
        if arr_re[k] != brr_re[k]:
            for x in range(brr_re[k] - arr_re[k]):
                a.append(k)
    a.sort()
    return a


# arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
# brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 205, 206, 204, 206]
# print(missingNumbers(arr, brr))

def all_factor(n):
    if n == 0:
        return [0]
    i = 1
    rlist = []
    while i <= n:
        if n % i == 0:
            rlist.append(i)
        i += 1
    return rlist


def get_total_x(a, b):
    bk_factor = {}
    for i in range(len(b)):
        bk_factor[b[i]] = all_factor(b[i])
    factor_va = list(bk_factor.values())
    allfactor = factor_va[0]
    for j in range(len(factor_va) - 1):
        allfactor_ = list(set(allfactor).intersection(set(factor_va[j + 1])))
        allfactor = allfactor_

    cc = []
    for c in allfactor:
        a_cou = 0
        for a_a in a:
            if c % a_a == 0:
                a_cou += 1
        if a_cou == len(a):
            cc.append(c)
    print(cc)
    return len(cc)


b = [16, 32, 96]
a = [2, 4]
print(get_total_x(a, b))

# print(all_factor(100))
