# coding:utf-8 
'''
created on 2019/2/23

@author:sunyihuan
'''
M, N = list(map(int, input().split(',')))
book = []
for i in range(M):
    line = list(map(int, input().split(',')))
    book.append(line)

print(book)