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

# //单个图片file,mode:1为检测最大的人脸 , 0为检测所有人脸
face = client.face_shape(CIFile('./test0.jpg'), 1)

# //单个图片Url,mode:1为检测最大的人脸 , 0为检测所有人脸
# face = client.face_shape(
#     CIUrl('https://xdimg.meiyezhushou.com/xiaomei/material_library/sample_face/2db161612335d559.jpg'), 1)

# 打印脸部数据
print(face["data"])

# 打印图片的高
print('image_height:', face["data"]["image_height"])
# 打印图片的宽
print('image_width:', face["data"]["image_width"])

# 打印轮廓数据（21个点）
print('face_profile', face["data"]["face_shape"][0]['face_profile'])
# 打印左眼数据（8个点）
print('left_eye', face["data"]["face_shape"][0]['left_eye'])
# 打印右眼数据（8个点）
print('right_eye', face["data"]["face_shape"][0]['right_eye'])
# 打印左眉数据（8个点）
print('left_eyebrow', face["data"]["face_shape"][0]['left_eyebrow'])
# 打印右眉数据（8个点）
print('right_eyebrow', face["data"]["face_shape"][0]['right_eyebrow'])
# 打印鼻子数据（13个点）
print('nose', face["data"]["face_shape"][0]['nose'])
# 打印嘴巴数据（22个点）
print('mouth', face["data"]["face_shape"][0]['mouth'])

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
plt.scatter(x=x, y=y, s=0.5, marker=".", c="r")
plt.show()
