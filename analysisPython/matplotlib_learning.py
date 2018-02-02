# coding:utf-8 
'''
created on 2018/2/1

@author:sunyihuan
'''

import matplotlib.pyplot as plt
from analysisPython.Titanic_predict.data_Handle import *
import seaborn as sns

file_train = "/Users/sunyihuan/Desktop/Data/Titanic/train.csv"
file_test = "/Users/sunyihuan/Desktop/Data/Titanic/test.csv"
train, test = handle_data(file_train=file_train, file_test=file_test)

x_train, y_train = XY_data(train)
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.33, random_state=1)
# x_train = data_normalization(x_train)
# x_test = data_normalization(x_test)
y_train = y_train.values.reshape(-1, 2)

# 创建一张图像,figsize=[4, 4]设置图像宽高为：6、6
plt.figure(num=1, figsize=[20, 20])

plt.subplot(336)

# 指定坐标轴的大小：[xmin, xmax, ymin, ymax]
plt.axis([0, 2, -1, 2])

# 点之间画线，默认蓝色，点没有特殊标
# plt.plot([y_train[i][0], -y_train[i][1]])

# 点之间画线，点以"o"的样式显示，线是虚线"--"，颜色为红色
plt.plot([y_train[0], -y_train[1]], "r--o")

# 显示图例，["y_train(0)", "y_train(1)"]显示的文本，'upper right'显示的位置
plt.legend(["y_train(0)", "y_train(1)"], loc='upper right')

# 设置X轴的文字
plt.xlabel('X')

# 设置Y轴的文字
plt.ylabel('Y')

# 设置图片标题
plt.title('point')

# 不显示坐标轴，axis中的参数有：equal、scaled、tight、auto等
# plt.axis('off')

# 第一个参数是x轴坐标
# 第二个参数是y轴坐标
# 第三个参数是要显式的内容
# alpha 设置字体的透明度
# family 设置字体
# size 设置字体的大小
# style 设置字体的风格
# wight 字体的粗细
# bbox 给字体添加框，alpha 设置框体的透明度， facecolor 设置框体的颜色
plt.text(0.1, 0.5, "point for y_train[{}]".format(1), size=10,
         family="fantasy", color="r", style="italic", weight="light",
         bbox=dict(facecolor="r", alpha=0.2))

# 保存图片，"picture/test.png"为图片地址和名称
plt.savefig("picture/test.png")
print(x_train.keys())

# 分成3x3个子图，占用第一个（横排数）
plt.subplot(331)  # the first subplot in the first figure

# 画直方图，x为输入的数据，bins为直方图的条数
plt.hist(x=x_train["Age"], bins=8)
plt.title('Age distribution')

# 分成3x3个子图，占用第二个（横排数）
plt.subplot(332)  # the first subplot in the first figure

# 画箱图
plt.boxplot(x=x_train["Age"])

plt.subplot(333)  # the first subplot in the first figure

# 画散点图
plt.scatter(x_train['Age'], x_train['Pclass'])

# 分成3x3个子图，占用第四个（横排数）
plt.subplot(334)  # the first subplot in the first figure

# 画小提琴图
sns.violinplot(x=x_train["family_member"])


# 分成3x3个子图，占用第九个（横排数）
plt.subplot(339)  # the first subplot in the first figure

# 画气泡图，s为气泡的大小
plt.scatter(x_train['Age'], x_train['Pclass'], s=x_train['family_member'])

# 创建第2张图
plt.figure(2)

# 分成3x1个子图，占用第一个（横排数）
plt.subplot(311)
plt.plot([1, 2, 3, 4])
plt.plot([2, 3, 4], [3, 5, 6], "g^")  # 一张图中画多条

# 分成3x1个子图，占用第三个（横排数）
plt.subplot(313)
plt.plot([1, 2, 3], [3, 2, 4], "r--", [2, 3, 4], [3, 5, 6], "g^")  # 用一条指令画多条不同格式的线

# 添加文本注释，'explaining'为文本，xy=(3, 4)为被注释的位置，xytext=(3.5, 5.5)为插入注释文本的地方
# arrowprops 用来设置箭头,facecolor为箭头为黄色， headlength为箭头的头的长度   headwidth为箭头的宽度  width为箭身的宽度
plt.annotate('explaining', xy=(3, 4), xytext=(3.5, 5.5),
             arrowprops=dict(facecolor='yellow', headlength=10, headwidth=25, width=10),
             )

plt.figure(3)
a = [15, 20, 30, 35]
labels = "apple", "banana", "pear", "yozi"
# 画饼图，a为数值，labels为标签
plt.pie(x=a, labels=labels)
# 设置坐标长宽一致
plt.axis("equal")

# 显示图像
plt.show()
