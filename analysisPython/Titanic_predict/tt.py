# coding:utf-8 
'''
created on 2018/1/31

@author:sunyihuan
'''

from analysisPython.Titanic_predict.data_Handle import *
import pandas as pd
from sklearn.decomposition import PCA

file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
train = pd.read_csv(file_train)
test = pd.read_csv(file_test)

pca = PCA(n_components='mle')
pca.fit(train)

print(pca.explained_variance_ratio_)
