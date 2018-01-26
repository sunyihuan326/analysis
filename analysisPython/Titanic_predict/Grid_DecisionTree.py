# coding:utf-8 
'''
created on 2018/1/26

@author:sunyihuan
'''

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from analysisPython.Titanic_predict.data_Handle import *
from sklearn.model_selection import GridSearchCV, StratifiedKFold


def model_Grid_DecisionTree(x_train, y_train, x_test, y_test):
    dectree = DecisionTreeClassifier(max_depth=5,
                                     class_weight="balanced",
                                     min_weight_fraction_leaf=0.01)
    max_depth = range(1, 10)
    max_feature = [1, 2, 3, 4, 5, 6, 7, 8, "auto"]
    grid3 = {'max_depth': max_depth, 'max_features': max_feature}
    decisiontree_grid = GridSearchCV(dectree, grid3, verbose=False,
                                     cv=StratifiedKFold(n_splits=5, random_state=15, shuffle=True))
    decisiontree_grid.fit(x_train, y_train)
    print(decisiontree_grid.best_params_)
    print(decisiontree_grid.best_score_)
    #
    # y_pre = decisiontree_grid.predict(x_test)
    # acurarcy = accuracy_score(y_true=y_test, y_pred=y_pre)
    # print(round(acurarcy, 3))
    return True


if __name__ == "__main__":
    file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
    file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
    train, test = handle_data(file_train=file_train, file_test=file_test)

    x_train, y_train = XY_data(train)
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.33, random_state=1)
    x_train = data_normalization(x_train)
    x_test = data_normalization(x_test)

    model_Grid_DecisionTree(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
