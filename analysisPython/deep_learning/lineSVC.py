# coding:utf-8
'''
Created on 2017/5/24

@author: sunyihuan
'''

# import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, cross_validation, svm
# import pandas as pd
# from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler


def load_data_classfication():
    iris = datasets.load_iris()
    X_train = iris.data
    Y_train = iris.target
    return cross_validation.train_test_split(X_train, Y_train, test_size=0.25, random_state=0, stratify=Y_train)


def test_SVC_linear(*data):
    X_train, X_tt, Y_train, Y_tt = data
    min_max_scaler = MinMaxScaler()
    X_train = min_max_scaler.fit_transform(X_train)
    Y_tt = min_max_scaler.fit_transform(X_tt)
    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, Y_train)
    print 'Coefficients:%s, intercept %s' % (clf.coef_, clf.intercept_)
    print 'Score:%.2f' % clf.score(X_tt, Y_tt)
    test_predict = clf.predict(X_tt)
    laber_list = list(test_predict)
    print laber_list
    clf.score(X_tt, Y_tt)
    print np.mean(test_predict == Y_tt)
    print Y_tt
    print test_predict
    # iris_test = pd.read_csv('E:/iris_test.csv')
    # X = iris_test[['aa', 'bb', 'cc', 'dd']]
    # Y = DataFrame(clf.predict(X), columns=['class'])
    # print X
    # print Y
    # # 把X_predict写入到iris_test.csv文件中。
    # XY = pd.concat([X, Y], axis=1)
    # print XY
    # Y=[X,X_predict]
    # print Y
    # XY.to_csv('E:/aa.csv', index=[])  # index=[]是为了在写入文件时，不把索引写入


if __name__ == "__main__":
    X_train, X_tt, Y_train, Y_tt = load_data_classfication()
    test_SVC_linear(X_train, X_tt, Y_train, Y_tt)
