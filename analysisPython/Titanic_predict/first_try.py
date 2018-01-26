# coding:utf-8 
'''
created on 2018/1/25

@author:sunyihuan
'''

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.model_selection import train_test_split

file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"

train = pd.read_csv(file_train)
test = pd.read_csv(file_test)
# print(train.info())
train.set_index("PassengerId", inplace=True)
test.set_index("PassengerId", inplace=True)

# print(train.head())

# print(train.info())
# print(test.info())

# print(train.isnull().sum())
# print(train.Embarked.value_counts(dropna=False))
# print(train.Embarked.value_counts(dropna=False, normalize=True) * 100)
train["Embarked"].fillna(value="S", inplace=True)
# print(train.Embarked.isnull().sum())
# print(train.Cabin.isnull().sum()/len(train.Cabin))
train.drop(labels=["Cabin"], axis=1, inplace=True)
test.drop(labels=['Cabin'], axis=1, inplace=True)

# print(test[test.Fare.isnull()])
# print((train.Age.isnull().sum() / len(train)) * 100)

# one-hot处理
train = pd.get_dummies(train, columns=['Embarked'])
train = pd.get_dummies(train, columns=['Sex'], drop_first=True)

# 某一列重命名
train = train.rename(columns={"Sex_male": "Gender"})

test = pd.get_dummies(test, columns=['Embarked'])
test = pd.get_dummies(test, columns=['Sex'], drop_first=True)
test = test.rename(columns={"Sex_male": "Gender"})

train.drop(['Name', 'Ticket'], axis=1, inplace=True)
test.drop(['Name', 'Ticket'], axis=1, inplace=True)

# print(test.isnull().sum())
from fancyimpute import KNN

age_train = KNN(k=10).complete(train)
# print(age_train)
train = pd.DataFrame(age_train, columns=train.columns)
# print(train.head(2))

test_index = test.index.values
age_test = KNN(k=10).complete(test)

test = pd.DataFrame(age_test, columns=test.columns)
# print(test.head(2))
test.index = test_index
# print(test.head(2))

survived_summary = train.groupby("Survived")
#
# survived_summary = train.groupby("Gender")

corr = train.corr() ** 2
# print(corr.Survived.sort_values(ascending=False))
# print(train.corr()['Survived'])
plt.subplots(figsize=(12, 10))
sns.heatmap(train.corr(),
            annot=True,
            linewidths=0.5,
            linecolor='white',
            square=True)
plt.title("Correlations Among Features", fontsize=20)
# plt.show()
avg_survived = train[train["Survived"] == 1]["Gender"].mean()
# print("The average Gender for the passengers who survived is: " + str(avg_survived))
avg_not_survived = train[train["Survived"] == 0]["Pclass"].mean()
# print("The average Gender for the passengers who did not survive is: " + str(avg_not_survived))

import scipy.stats as stats

stats.ttest_1samp(a=train[train['Survived'] == 1]['Gender'],
                  popmean=avg_not_survived)

degree_freedom = len(train[train['Survived'] == 1])

LQ = stats.t.ppf(0.025, degree_freedom)  # Left Quartile

RQ = stats.t.ppf(0.975, degree_freedom)  # Right Quartile

# print('The left quartile range of t-distribution is: ' + str(LQ))
# print('The right quartile range of t-distribution is: ' + str(RQ))


# Gender and Survived
plt.subplots(figsize=(15, 8))
sns.barplot(x="Gender", y="Survived", data=train, linewidth=2)
plt.title("Survived/Non-Survived Passenger Gender Distribution", fontsize=25)
plt.ylabel("% of passenger survived", fontsize=15)
plt.xlabel("Gender", fontsize=15)

labels = ['Female', 'Male']
plt.xticks(sorted(train.Gender.unique()), labels)
# plt.show()

sns.set(style="darkgrid")
plt.subplots(figsize=(15, 8))
ax = sns.countplot(x="Gender",
                   hue="Survived",
                   data=train,
                   edgecolor=(0, 0, 0),
                   linewidth=2)
## Fixing title, xlabel and ylabel
plt.title("Passenger Gender Distribution - Survived vs Not-survived", fontsize=25)
plt.xlabel("Gender", fontsize=15);
plt.ylabel("# of Passenger Survived", fontsize=15)

## Fixing xticks
labels = ['Female', 'Male']
plt.xticks(sorted(train.Gender.unique()), labels)

## Fixing legends
leg = ax.get_legend()
leg.set_title("Survived")
legs = leg.texts
legs[0].set_text("No")
legs[1].set_text("Yes")

# Pclass and Survived
plt.subplots(figsize=(15, 10))
sns.barplot(x="Pclass", y="Survived", data=train, edgecolor=(0, 0, 0), linewidth=2)
plt.title("Passenger Class Distribution - Survived vs Non-Survived", fontsize=25)
plt.xlabel("Socio-Economic class", fontsize=15)
plt.ylabel("% of Passenger Survived", fontsize=15)
train.loc[(train['Survived'] == 0), 'Pclass'].head()

fig = plt.figure(figsize=(15, 8), )
## I have included to different ways to code a plot below, choose the one that suites you.
ax = sns.kdeplot(train.Pclass[train.Survived == 0], color='r', shade=True, label='not survived')
ax = sns.kdeplot(train.loc[(train['Survived'] == 1), 'Pclass'], color='g', shade=True, label='survived')
plt.title('Passenger Class Distribution - Survived vs Non-Survived', fontsize=25)
plt.ylabel("Frequency of Passenger Survived", fontsize=15)
plt.xlabel("Passenger Class", fontsize=15)
## Converting xticks into words for better understanding
labels = ['First', 'Second', 'Third']
plt.xticks(sorted(train.Pclass.unique()), labels)

# Fare and Survived
fig = plt.figure(figsize=(15, 8), )
ax = sns.kdeplot(train.loc[(train['Survived'] == 0), 'Fare'], color='r', shade=True, label='not survived')
ax = sns.kdeplot(train.loc[(train['Survived'] == 1), 'Fare'], color='g', shade=True, label='survived')
plt.title('Fare Distribution Survived vs Non Survived', fontsize=25)
plt.ylabel("Frequency of Passenger Survived", fontsize=15)
plt.xlabel("Fare", fontsize=15)

# Age and Survived
fig = plt.figure(figsize=(15, 8), )
ax = sns.kdeplot(train.loc[(train['Survived'] == 0), 'Age'], color='r', shade=True, label='not survived')
ax = sns.kdeplot(train.loc[(train['Survived'] == 1), 'Age'], color='g', shade=True, label='survived')
plt.title('Age Distribution - Surviver V.S. Non Survivors')
plt.xlabel("Age", fontsize=15)
plt.ylabel('Frequency', fontsize=15);
# plt.show()

# print(train.columns)

# child featurs
train['child'] = [1 if i < 18 else 0 for i in train.Age]
test['child'] = [1 if i < 18 else 0 for i in test.Age]

# family member feature
train['family_member'] = train.SibSp + train.Parch
test['family_member'] = test.SibSp + test.Parch
# print(train.head(2))
train['is_alone'] = [1 if i < 2 else 0 for i in train.family_member]
test['is_alone'] = [1 if i < 2 else 0 for i in test.family_member]


print("train.shape", train.shape)

print(train.head(2))

print("$$$$$$%%%%%^^^^^^^_____+++++++++++++++++++++++++")

# Modeling the Data
X = train.drop(['Survived'], axis=1)
y = train["Survived"]
print("X.shape", X.shape)
print(X.head(2))
# print(X.head(1))
# print(y.head(1))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=1)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
final_test = sc.transform(test)
print("x_train.shape")
print(x_train.shape)
print(y_train.shape)

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_recall_curve, confusion_matrix
from sklearn.linear_model import LogisticRegression

# LogisticRegression
logreg = LogisticRegression(solver='liblinear', penalty='l1')
logreg.fit(x_train, y_train)
y_pred = logreg.predict(x_test)
logreg_accy = round(accuracy_score(y_pred, y_test), 3)
print(logreg_accy)
print(classification_report(y_test, y_pred, labels=logreg.classes_))
print(confusion_matrix(y_pred, y_test))

C_vals = [0.0001, 0.001, 0.01, 0.1, 0.13, 0.2, .15, .25, .275, .33, 0.5, .66, 0.75, 1.0, 2.5, 4.0, 4.5, 5.0, 5.1, 5.5,
          6.0, 10.0, 100.0, 1000.0]
penalties = ['l1', 'l2']

param = {'penalty': penalties, 'C': C_vals, }
grid = GridSearchCV(logreg, param, verbose=False, cv=StratifiedKFold(n_splits=5, random_state=15, shuffle=True),
                    n_jobs=1)
grid.fit(x_train, y_train)
print(grid.best_params_)
print(grid.best_score_)

logreg_grid = LogisticRegression(penalty=grid.best_params_['penalty'], C=grid.best_params_['C'])
logreg_grid.fit(x_train, y_train)
y_pred = logreg_grid.predict(x_test)
logreg_accy = round(accuracy_score(y_test, y_pred), 3)
print("penalty", logreg_accy)
print(classification_report(y_test, y_pred, labels=logreg_grid.classes_))

# roc curve
from sklearn.metrics import roc_curve, auc

plt.style.use('seaborn-pastel')
y_score = logreg_grid.decision_function(x_test)

FPR, TPR, _ = roc_curve(y_test, y_score)
ROC_AUC = auc(FPR, TPR)
print(ROC_AUC)

plt.figure(figsize=[11, 9])
plt.plot(FPR, TPR, label='ROC curve(area = %0.2f)' % ROC_AUC, linewidth=4)
plt.plot([0, 1], [0, 1], 'k--', linewidth=4)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate', fontsize=18)
plt.ylabel('True Positive Rate', fontsize=18)
plt.title('ROC for Titanic survivors', fontsize=18)

plt.style.use('seaborn-pastel')

y_score = logreg_grid.decision_function(x_test)

precision, recall, _ = precision_recall_curve(y_test, y_score)
PR_AUC = auc(recall, precision)

plt.figure(figsize=[11, 9])
plt.plot(recall, precision, label='PR curve (area = %0.2f)' % PR_AUC, linewidth=4)
plt.xlabel('Recall', fontsize=18)
plt.ylabel('Precision', fontsize=18)
plt.title('Precision Recall Curve for Titanic survivors', fontsize=18)
plt.legend(loc="lower right")
# plt.show()


# knn
from sklearn.neighbors import KNeighborsClassifier

print(x_train.shape, y_train.shape)
print(x_train[1], y_train[1])
print("______++++++++++++$$$$$$$$$$$")

knn = KNeighborsClassifier(weights="uniform", )
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
knn_accy = round(accuracy_score(y_test, y_pred), 3)
print(knn_accy)

knn = KNeighborsClassifier()
n_neighbors = range(1, 10)
weights = ['uniform', 'distance']
param = {'n_neighbors': n_neighbors, 'weights': weights}
grid2 = GridSearchCV(knn, param, verbose=False, cv=StratifiedKFold(n_splits=5, random_state=15, shuffle=True))
grid2.fit(x_train, y_train)
print(grid2.best_params_)
print(grid2.best_score_)

knn_grid = KNeighborsClassifier(
    n_neighbors=grid2.best_params_['n_neighbors'],
    weights=grid2.best_params_['weights'],
    n_jobs=1,
)
knn_grid.fit(x_train, y_train)
y_pred = knn_grid.predict(x_test)
knn_accy = round(accuracy_score(y_test, y_pred), 3)
print(knn_accy)
