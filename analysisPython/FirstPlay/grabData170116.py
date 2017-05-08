# coding:utf-8
'''
Created on 2017/1/16

@author: sunyihuan
'''
import requests
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


urls = []
for i in list(range(1, 10)):
    urls.append(
        'https://rate.tmall.com/list_detail_rate.htm?itemId=521136254098&spuId=345965243&sellerId=2106525799&order=1&currentPage=%s' % i)

nickname = []
ratedate = []
color = []
size = []
ratecontent = []

for url in urls:
    content = requests.get(url).text

    nickname.extend(re.findall('"displayUserNick":"(.*?)"', content))
    color.extend(re.findall(re.compile('颜色分类:(.*?);'), content))
    size.extend(re.findall(re.compile('尺码:(.*?);'), content))
    ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'), content))
    ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'), content))
    # print nickname

print len(nickname)
file = open('nanjiren.csv', 'w')
for i in range(len(nickname)):
    print nickname[i]
    # print i
    # file.write(str(1))
    file.write(','.join((unicode(nickname[i]))) + '\n')
file.close()
