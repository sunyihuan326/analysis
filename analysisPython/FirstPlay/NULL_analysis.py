# coding:utf-8
'''
Created on 2016/11/21

@author: sunyihuan
'''
import pymysql
import time

conn = pymysql.connect(host="rdsea8n4lglktg5e69p.mysql.rds.aliyuncs.com", user="yanshan", passwd="pwd_yanshan2016",
                       db="yanshan_db", port=3306, charset='utf8')  # 链接数据库
cur = conn.cursor()  # 获取游标

#  原生态sql语句

sql3 = "select * from ys_order WHERE status=1 LIMIT 100"


cur.execute(sql3)
data=cur.fetchall()
for d in data:
    t=time.strptime('',d[-2])
    print d[-2]