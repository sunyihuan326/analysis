# coding:utf-8 
'''
created on 2018/1/31

@author:sunyihuan
'''

from analysisPython.Titanic_predict.data_Handle import *

file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
train, test = handle_data(file_train=file_train, file_test=file_test)

x_train, y_train = XY_data(train)
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.33, random_state=1)

print(x_train.shape)
print(x_train.shape[1])
