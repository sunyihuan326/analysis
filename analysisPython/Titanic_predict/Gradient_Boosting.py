# coding:utf-8 
'''
created on 2018/1/26

@author:sunyihuan
'''

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from analysisPython.Titanic_predict.data_Handle import *
from sklearn.model_selection import GridSearchCV, StratifiedKFold


def model_GradientBoosting(x_train, y_train, x_test, y_test):
    GradientBoosting = GradientBoostingClassifier()
    GradientBoosting.fit(x_train, y_train)
    y_pre = GradientBoosting.predict(x_test)
    acurarcy = accuracy_score(y_true=y_test, y_pred=y_pre)
    print(round(acurarcy, 3))
    return True


if __name__ == "__main__":
    file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
    file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
    train, test = handle_data(file_train=file_train, file_test=file_test)

    x_train, y_train = XY_data(train)
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.33, random_state=1)
    x_train = data_normalization(x_train)
    x_test = data_normalization(x_test)

    model_RandomForest(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
