# coding:utf-8 
'''
created on 2018/2/5

@author:sunyihuan
'''

from PIL import Image

# 打开图片
img_pie = Image.open("pie_picture.jpg")
img_scatter = Image.open("scatter_picture.jpg")

# 新建图片
newImage = Image.new(mode="RGBA", size=(600, 700), color=(0, 100, 200))

# 查看图片
# newImage.show()

# 查看图片大小
pie_w, pie_h = img_pie.size

# 重新设置图片大小
new_scatter = img_scatter.resize((pie_w, pie_h))
# new_scatter.show()

# 将两张图片相加，alpha为比例参数
two_picture = Image.blend(img_pie, new_scatter, alpha=0.2)
# two_picture.show()

# 裁剪图片的某一区域
box = (100, 200, 300, 500)
region = img_scatter.crop(box)
# region.show()

# 图像转换
sa = region.rotate(45)
region = region.transpose(Image.ROTATE_180)

# 图像左右兑换
out = region.transpose(Image.FLIP_TOP_BOTTOM)

# 图像合并
img_pie.paste(region, box)
# img_pie.show()

# 图像通道分离
r, g, b = img_pie.split()
# b.show()

# 图像类型转换
im = img_pie.convert("RGBA")
# im.show()

# 获取某个像素位置的值
a = im.getpixel((40, 200))
print(a)

# 给某个像素赋值
im.putpixel((4, 4), (0, 0, 0, 0))
im.show()
