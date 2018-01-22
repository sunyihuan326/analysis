# coding:utf-8
'''
Created on 2016/10/22

@author: sunyihuan
'''

# while循环
s = 0
k = 0
while k < 101:
    k = k + 1
    s = s + k
print(s)

# lamnbda定义函数
f = lambda x, y: x + y
print (f(2, 6))

# 列表
c = [1, 'abc', [1, 2]]
print( c[1], c[2][1])

# 字典
d = {'today': 20, 'tomorrow': 30}
print(d['today'])

from scipy.optimize import fsolve


# 求解非线性方程组
def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2 * x1 - x2 ** 2 - 1, x1 ** 2 - x2 - 2]


result = fsolve(f, [1, 1])
print(result)

# 积分
from scipy import integrate


def g(x):
    return (1 - x ** 2) ** 0.5


pi_2, err = integrate.quad(g, 0, 1)
print(pi_2)

import pandas as pd

s = pd.Series([1, 2, 3], index=["a", "b", "c"])
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "b", "c"])
d2 = pd.DataFrame(s)
d.head()
print(d.describe())
