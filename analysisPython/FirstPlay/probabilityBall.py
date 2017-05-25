# coding:utf-8
'''
Created on 2017/5/25

@author: sunyihuan
'''

import random


class SelectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = raw_input('请输入测试数据：')
            try:
                num = int(numStr)

            except ValueError:
                print u'要求输入一个整数'
                continue
            else:
                break
        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in xrange(num):
            n = random.randint(1, 10)
            ball[n - 1] += 1
        for i in xrange(1, 11):
            print u'获取第%d号球的概率为%f' % (i, ball[i - 1] * 1.0 / num)


if __name__ == '__main__':
    S = SelectBall()
