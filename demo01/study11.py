# -*- coding: utf-8 -*-
'''
 本demo主要介绍PIL一些常用的操作，裁剪，旋转，保存，修改尺寸等等
'''
from PIL import Image
import sys
# 为l引入imtools，返回到上一层
sys.path.append("..")
import tools.imtools
'''
读取一张图片
'''
im = Image.open('image.jpeg');
# 1 ----设置灰色-----
im = im.convert('L');
# 2 ----保存图片-----
im.save('image_grey.jpeg');
#获取当前文档下所有的jpg图片列表
print(tools.imtools.get_imlist('./'));

# 3 ----图片缩略图-----
im.thumbnail((128,128));
im.save('image_thumbail.jpeg');

# 4 ----对图像进行裁剪-----
im1 = Image.open('image.jpeg');
box = (100,100,400,400);
region = im1.crop(box);
region.save('image_crop.jpeg');

# 5 -----旋转图片执行区域-----
im2 = Image.open('image.jpeg');
box = (100,100,400,400);
# 获取执行区域
region = im2.crop(box);
# 对制定区域旋转
region = region.transpose(Image.ROTATE_180);
# 把旋转的区域重新贴回原图
im2.paste(region,box);
im2.save('image_rotate.jpeg');

# 6 ------调整尺寸和旋转------
im3 = Image.open('image.jpeg');
im3 = im3.resize((400,400));
im3 = im3.rotate(45);
im3.save('image_resize_rotate.jpeg');



