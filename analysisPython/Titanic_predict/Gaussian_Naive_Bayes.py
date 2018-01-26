# coding:utf-8 
'''
created on 2018/1/26

@author:sunyihuan
'''

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from analysisPython.Titanic_predict.data_Handle import *


def model_Gaussian_Naive_Bayes(x_train, y_train, x_test, y_test):
    gaussian = GaussianNB()
    gaussian.fit(x_train, y_train)
    y_pred = gaussian.predict(x_test)
    gaussian_accy = round(accuracy_score(y_pred, y_test), 3)
    print(gaussian_accy)
    return True


if __name__ == "__main__":
    file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
    file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
    train, test = handle_data(file_train=file_train, file_test=file_test)

    x_train, y_train = XY_data(train)
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.33, random_state=1)
    x_train = data_normalization(x_train)
    x_test = data_normalization(x_test)

    model_Gaussian_Naive_Bayes(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
