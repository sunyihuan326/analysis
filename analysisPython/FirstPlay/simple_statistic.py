# coding:utf-8
'''
Created on 2017/2/20

@author: sunyihuan
'''
import pandas as pd

D = pd.DataFrame([range(1, 8), range(2, 9)])
D.corr(method='spearman')
s1 = D.loc[0]
s2 = D.loc[1]
print(s1.corr(s2, method='pearson'))
