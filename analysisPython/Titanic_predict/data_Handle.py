# coding:utf-8 
'''
created on 2018/1/25

@author:sunyihuan
'''
import pandas as pd
from fancyimpute import KNN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def handle_data(file_train, file_test):
    train = pd.read_csv(file_train)
    test = pd.read_csv(file_test)

    train.set_index("PassengerId", inplace=True)
    test.set_index("PassengerId", inplace=True)


    train["Embarked"].fillna(value="S", inplace=True)
    train.drop(labels=["Cabin"], axis=1, inplace=True)
    test.drop(labels=['Cabin'], axis=1, inplace=True)

    train = pd.get_dummies(train, columns=['Embarked'])
    train = pd.get_dummies(train, columns=['Sex'], drop_first=True)
    train = train.rename(columns={"Sex_male": "Gender"})

    test = pd.get_dummies(test, columns=['Embarked'])
    test = pd.get_dummies(test, columns=['Sex'], drop_first=True)
    test = test.rename(columns={"Sex_male": "Gender"})

    train.drop(['Name', 'Ticket'], axis=1, inplace=True)
    test.drop(['Name', 'Ticket'], axis=1, inplace=True)

    age_train = KNN(k=10).complete(train)
    # print(age_train)
    train = pd.DataFrame(age_train, columns=train.columns)

    age_test = KNN(k=10).complete(test)

    test = pd.DataFrame(age_test, columns=test.columns)

    train['child'] = [1 if i < 18 else 0 for i in train.Age]
    test['child'] = [1 if i < 18 else 0 for i in test.Age]

    # family member feature
    train['family_member'] = train.SibSp + train.Parch
    test['family_member'] = test.SibSp + test.Parch
    # print(train.head(2))
    train['is_alone'] = [1 if i < 2 else 0 for i in train.family_member]
    test['is_alone'] = [1 if i < 2 else 0 for i in test.family_member]
    return train, test


def XY_data(train):
    X = train.drop(['Survived'], axis=1)
    Y = train["Survived"]
    return X, Y


def data_split(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.33, random_state=1)
    return x_train, x_test, y_train, y_test


def data_normalization(data):
    sc = StandardScaler()
    data = sc.fit_transform(data)
    return data
