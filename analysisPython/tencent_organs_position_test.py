# coding:utf-8 
'''
created on 2018/2/27

@author:sunyihuan
'''

from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 腾讯云获得
appid = '1256126369'
secret_id = 'AKIDENK7iBfpOn160lzxRk1FJEykOrPwn3Tu'
secret_key = 'c9VfecUExb7YwFXjpttnmkhZL1b6QccU'
bucket = 'test0'

client = Client(appid, secret_id, secret_key, bucket)
client.use_http()
client.set_timeout(30)

# //单个图片Url,mode:1为检测最大的人脸 , 0为检测所有人脸
face = client.face_shape(
    CIUrl('https://xdimg.meiyezhushou.com/xiaomei/material_library/sample_face/2db161612335d559.jpg'), 1)
print(face["data"])
print(face["data"]["face_shape"][0]['face_profile'])

x = []
y = []
# 获取脸型轮廓点
for i in range(len(face["data"]["face_shape"][0]['face_profile'])):
    x_ = face["data"]["face_shape"][0]['face_profile'][i]["x"]
    y_ = face["data"]["face_shape"][0]['face_profile'][i]["y"]
    x.append(x_)
    y.append(y_)
print("x", x)
print("y", y)
img = mpimg.imread("test0.jpg")
plt.imshow(img)
plt.scatter(x=x, y=y, s=0.5, marker=".")
plt.show()

# x = face["data"]["face_shape"][0]['face_profile'][0]["x"]
# print(x)

# //单个图片file,mode:1为检测最大的人脸 , 0为检测所有人脸
# print(client.face_shape(CIFile('./test0.jpg'), 1))
