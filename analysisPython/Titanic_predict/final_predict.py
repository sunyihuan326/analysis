# coding:utf-8 
'''
created on 2018/1/26

@author:sunyihuan
'''
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score, classification_report, precision_recall_curve, confusion_matrix
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split, StratifiedKFold
from analysisPython.Titanic_predict.data_Handle import *
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from sklearn.linear_model import LogisticRegression


class model_all():
    def __init__(self, x_train, y_train, x_test, y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.n_x = x_train.shape[1]

    def model_Logistic(x_train, y_train, x_test, y_test):
        logistc = LogisticRegression()
        logistc.fit(x_train, y_train)
        y_pred = logistc.predict(x_test)
        accurarcy = round(accuracy_score(y_test, y_pred), 3)
        print("accurarcy", accurarcy)
        return logistc

    def model_knn(x_train, y_train, x_test, y_test):
        knn = KNeighborsClassifier(weights="uniform")
        knn.fit(x_train, y_train)
        y_pred = knn.predict(x_test)
        knn_accy = round(accuracy_score(y_test, y_pred), 3)
        print("accurarcy", knn_accy)
        return knn

    def model_Grid_knn(x_train, y_train, x_test, y_test):
        knn = KNeighborsClassifier()
        n_neighbors = range(1, 10)
        weights = ['uniform', 'distance']
        param = {'n_neighbors': n_neighbors, 'weights': weights}
        grid2 = GridSearchCV(knn, param, verbose=False, cv=StratifiedKFold(n_splits=5, random_state=15, shuffle=True))
        grid2.fit(x_train, y_train)
        knn_grid = KNeighborsClassifier(
            n_neighbors=grid2.best_params_['n_neighbors'],
            weights=grid2.best_params_['weights'],
            n_jobs=1,
        )
        knn_grid.fit(x_train, y_train)
        y_pred = knn_grid.predict(x_test)
        knn_accy = round(accuracy_score(y_test, y_pred), 3)
        print("accurarcy", knn_accy)
        return knn_grid

    def model_Gaussian_Naive_Bayes(x_train, y_train, x_test, y_test):
        gaussian = GaussianNB()
        gaussian.fit(x_train, y_train)
        y_pred = gaussian.predict(x_test)
        gaussian_accy = round(accuracy_score(y_pred, y_test), 3)
        print("accurarcy", gaussian_accy)
        return gaussian

    def model_DecisionTree_Classifier(x_train, y_train, x_test, y_test):
        dectree = DecisionTreeClassifier(max_depth=5,
                                         class_weight="balanced",
                                         min_weight_fraction_leaf=0.01)
        dectree.fit(x_train, y_train)
        y_pre = dectree.predict(x_test)
        accurarcy = round(accuracy_score(y_pred=y_pre, y_true=y_test))
        print("accurarcy", accurarcy)
        return dectree

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
        # print(decisiontree_grid.best_params_)
        # print(decisiontree_grid.best_score_)
        # #
        y_pre = decisiontree_grid.predict(x_test)
        acurarcy = accuracy_score(y_true=y_test, y_pred=y_pre)
        print("accurarcy", round(acurarcy, 3))
        return decisiontree_grid

    def model_GradientBoosting(x_train, y_train, x_test, y_test):
        GradientBoosting = GradientBoostingClassifier()
        GradientBoosting.fit(x_train, y_train)
        y_pre = GradientBoosting.predict(x_test)
        acurarcy = accuracy_score(y_true=y_test, y_pred=y_pre)
        print("accurarcy", round(acurarcy, 3))
        return GradientBoosting

    def model_svc(x_train, y_train, x_test, y_test):
        svc = SVC()
        svc.fit(x_train, y_train)
        y_pred = svc.predict(x_test)
        svc_accy = round(accuracy_score(y_pred, y_test), 3)
        print("accurarcy", svc_accy)

        return svc

    def model_RandomForest(x_train, y_train, x_test, y_test):
        randomForest = RandomForestClassifier()
        randomForest.fit(x_train, y_train)
        y_pre = randomForest.predict(x_test)
        acurarcy = accuracy_score(y_true=y_test, y_pred=y_pre)
        print("accurarcy", round(acurarcy, 3))
        return randomForest


if __name__ == "__main__":
    file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
    file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
    train, test = handle_data(file_train=file_train, file_test=file_test)

    x_train, y_train = XY_data(train)
    x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.33, random_state=1)
    x_train = data_normalization(x_train)
    x_test = data_normalization(x_test)

    alg = model_all.model_Grid_knn(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)

    y = alg.predict(test)
    # print(y)
