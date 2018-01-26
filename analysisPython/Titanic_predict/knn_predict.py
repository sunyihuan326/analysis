# coding:utf-8 
'''
created on 2018/1/25

@author:sunyihuan
'''

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score, classification_report, precision_recall_curve, confusion_matrix
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split, StratifiedKFold
from analysisPython.Titanic_predict.data_Handle import *


def model_knn(x_train, y_train, x_test, y_test):
    knn = KNeighborsClassifier(weights="uniform")
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    knn_accy = round(accuracy_score(y_test, y_pred), 3)
    print(knn_accy)

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
