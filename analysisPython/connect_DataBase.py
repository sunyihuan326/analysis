# coding:utf-8 
'''
created on 2018/2/23

@author:sunyihuan
'''

import pymysql
import pymongo
import urllib.parse


def connect_mysql(host, user, pwd, port, db):
    # 连接数据库，需要输入地址、用户名、密码、端口、数据库名称
    db = pymysql.connect(host=host, user=user,
                         password=pwd, port=port, database=db)
    # 创建游标
    cursor = db.cursor()

    # 执行sql，返回受影响的行数
    effect_row = cursor.execute("select * from ys_user")
    # print("rows", effect_row)

    # 执行剩余结果的第一行
    r_1 = cursor.fetchone()
    # print("fetchone", r_1)

    # 执行剩余结果的前3行
    r_3 = cursor.fetchmany(3)
    # print("r_3", r_3)

    # 执行剩余结果的所有行
    r_all = cursor.fetchall()
    # print(r_all)
    return True


host = "rdsea8n4lglktg5e69p1o.mysql.rds.aliyuncs.com"
user = "shuwei_test"
pwd = "pwd_test2016"
port = 3306
db = "yanshan_test"

connect_mysql(host=host, user=user, pwd=pwd, port=port, db=db)


def connect_mongodb(user, pwd):
    # 用户认证名称、密码
    username = urllib.parse.quote_plus(user)
    password = urllib.parse.quote_plus(pwd)

    # 建立和mongodb数据库系统的连接
    client = pymongo.MongoClient('mongodb://%s:%s@dev.yanzijia.cn' % (username, password))

    # 连接目标数据库
    db = client.yanshan_test

    # 连接目标集合
    col = db["question"]

    # 打印集合第一条
    print(col.find_one())

    return True


user = "yanzi"
pwd = "yanzi2016"
connect_mongodb(user=user, pwd=pwd)
