# coding:utf-8 
'''
created on 2018/1/25

@author:sunyihuan
'''
import pandas as pd
from fancyimpute import KNN, SoftImpute
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
    # print("age before", train["Age"])

    # 将train中的nan以SoftImpute方式填充
    age_train = SoftImpute().complete(train)
    # age_train = KNN(k=8).complete(train)

    # print(age_train)
    train = pd.DataFrame(age_train, columns=train.columns)
    # print("train", train["Age"])
    # print(train.isnull().sum())

    # 将test中的nan以SoftImpute方式填充
    age_test = SoftImpute().complete(test)

    test = pd.DataFrame(age_test, columns=test.columns)

    # 记录是否是孩子,小于18记为1，其他记为0
    train['child'] = [1 if i < 18 else 0 for i in train.Age]
    test['child'] = [1 if i < 18 else 0 for i in test.Age]

    # family member feature
    train['family_member'] = train.SibSp + train.Parch
    test['family_member'] = test.SibSp + test.Parch

    # 记录是否一个人,family_member小于2记为1，其他记为0
    train['is_alone'] = [1 if i < 2 else 0 for i in train.family_member]
    test['is_alone'] = [1 if i < 2 else 0 for i in test.family_member]
    return train, test


def XY_data(train):
    # 去掉所有Survived项为X
    X = train.drop(['Survived'], axis=1)

    # Survived为Y
    Y = train["Survived"]
    return X, Y


def data_split(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.33, random_state=1)
    return x_train, x_test, y_train, y_test


def data_normalization(data):
    # 去均值和方差归一化
    sc = StandardScaler()

    # 先拟合数据，然后转化它将其转化为标准形式
    data = sc.fit_transform(data)
    return data


# file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
# file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
# train, test = handle_data(file_train=file_train, file_test=file_test)
