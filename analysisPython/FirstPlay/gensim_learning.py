# coding:utf-8
'''
Created on 2016/11/21

@author: sunyihuan
'''
import gensim,logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
sentence=[['first','sentence'],['second','sentence']]
model=gensim.models.Word2Vec(sentence,min_count=1)
print(model['sentence'])