# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 测试python处理图片的支持python3.x的库pillow
from PIL import Image, ImageFilter


def generate_thumbnail():  # 生成缩略图
    image = Image.open('ZYJ.jpg')  # 打开图像文件
    weiht, height = image.size
    print('图片的高为：', height, '图像的宽为：', weiht)
    image.thumbnail((weiht // 2, height // 2))
    image.save('ZYJ-thumbnail.jpg', 'jpeg')  # 保存缩略图文件


def filter_image():  # 添加模糊效果
    image = Image.open('ZYJ.jpg')
    filter_img = image.filter(ImageFilter.BLUR)
    filter_img.save('ZYJ-filter-blur.jpg', 'jpeg')

# piilow的详情地址：https://pillow.readthedocs.org/
if __name__ == '__main__':
    filter_image()

