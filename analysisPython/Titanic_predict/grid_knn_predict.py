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
    knn = KNeighborsClassifier()
    n_neighbors = range(1, 10)
    weights = ['uniform', 'distance']
    param = {'n_neighbors': n_neighbors, 'weights': weights}
    grid2 = GridSearchCV(knn, param, verbose=False, cv=StratifiedKFold(n_splits=5, random_state=15, shuffle=True))
    grid2.fit(x_train, y_train)
    # print(grid2.best_params_)
    # print(grid2.best_score_)

    knn_grid = KNeighborsClassifier(
        n_neighbors=grid2.best_params_['n_neighbors'],
        weights=grid2.best_params_['weights'],
        n_jobs=1,
    )
    knn_grid.fit(x_train, y_train)
    y_pred = knn_grid.predict(x_test)
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
