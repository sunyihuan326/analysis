# coding:utf-8 
'''
created on 2018/1/25

@author:sunyihuan
'''
import pandas as pd
from fancyimpute import KNN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder


def handle_data(file_train, file_test):
    # pandas加载csv数据
    train = pd.read_csv(file_train)
    test = pd.read_csv(file_test)

    # 设置PassengerId为索引，inplace=True索引为列
    train.set_index("PassengerId", inplace=True)
    test.set_index("PassengerId", inplace=True)

    # 将Embarked中的nan填充为"S"
    train["Embarked"].fillna(value="S", inplace=True)

    # 按列删除Cabin
    train.drop(labels=["Cabin"], axis=1, inplace=True)
    test.drop(labels=['Cabin'], axis=1, inplace=True)

    # 查看表中字段
    train.keys()

    # 对train中Embarked列进行one-hot编码
    train = pd.get_dummies(train, columns=['Embarked'])
    train = pd.get_dummies(train, columns=['Sex'], drop_first=True)

    # 重新命名Sex_male列为Gender
    train = train.rename(columns={"Sex_male": "Gender"})

    # test-hot编码
    test = pd.get_dummies(test, columns=['Embarked'])
    test = pd.get_dummies(test, columns=['Sex'], drop_first=True)

    # 重新命名Sex_male列为Gender
    test = test.rename(columns={"Sex_male": "Gender"})

    # 删除Name、Ticket两列
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


file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
train, test = handle_data(file_train=file_train, file_test=file_test)
