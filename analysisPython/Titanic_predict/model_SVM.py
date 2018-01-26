# coding:utf-8 
'''
created on 2018/1/26

@author:sunyihuan
'''
from analysisPython.Titanic_predict.data_Handle import *
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def model_knn(x_train, y_train, x_test, y_test):
    svc = SVC()
    svc.fit(x_train, y_train)
    y_pred = svc.predict(x_test)
    svc_accy = round(accuracy_score(y_pred, y_test), 3)
    print(svc_accy)

    return True


if __name__ == "__main__":
    file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
    file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
    train, test = handle_data(file_train=file_train, file_test=file_test)

    x_train, y_train = XY_data(train)
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.33, random_state=1)
    x_train = data_normalization(x_train)
    x_test = data_normalization(x_test)

    model_knn(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
