# coding:utf-8
'''
Created on 2017/5/25

@author: sunyihuan
'''
import os


def operaFile():  # 创建文件
    print("^^^^^^^")
    print('a')
    print(u'先保证该文件不存在')
    os.system('rm text.txt')
    os.system('ls -l test.txt')
    fp = open('text.txt', 'w')
    fp.write('Hello Python')
    fp.close()
    os.system('ls -l test.txt')
    os.system('cat test.txt')
    print('\n')

    with open('text.txt', 'r') as fp:
        st = fp.read()
    print('text.txt的内容为：%s' % st)


if __name__ == '__mian__':
    operaFile()
