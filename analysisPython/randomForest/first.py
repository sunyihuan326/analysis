# coding:utf-8
'''
Created on 2016/12/1

@author: sunyihuan
'''
import numpy as np
import pylab as pl

x = np.random.uniform(1, 100, 100)
y = np.log(x) + np.random.normal(0, .3, 100)
pl.scatter(x, y, s=1, label="log(x) with noise")
pl.plot(np.arange(1, 100), np.log(np.arange(1, 100)))
pl.xlabel("x")
pl.ylabel("f(x)=log(x)")
pl.legend(loc="best")
pl.show()
