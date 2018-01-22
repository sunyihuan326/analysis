# coding:utf-8
'''
Created on 2016/11/21

@author: sunyihuan
'''
from statsmodels.tsa.stattools import adfuller as ADF
import numpy as np

from sklearn import svm, datasets

print(ADF(np.random.rand(100)))
iris = datasets.load_iris()
# print (iris.data.shape)

clf = svm.LinearSVC()
clf.fit(iris.data, iris.target)
clf.predict([[5.0, 3.6, 1.3, 0.25]])
print(clf.coef_)
