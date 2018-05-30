# -*- coding: utf-8 -*-
'''
 本demo主要介绍numpy介绍
'''
from  PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
# 为l引入imtools，返回到上一层
sys.path.append("..")
import tools.imtools

def test():
	im = Image.open('image.jpeg').convert('L');
	im = array(im); #讲image转数组
	imm = Image.fromarray(im); # 将array转image对象
	im2 = 255 - im ;      # 像素翻转
	im2 = Image.fromarray(im2)
	im3 = (100.0/255)*im+100;  # 100到200之间
	im3 = Image.fromarray(im3)
	im4 = 255.0*(im/255.0)**2;  # 像素求平方
	im4 = Image.fromarray(im4)
	imshow(im3);
	show();
	pass;

#缩放操作	
def test2():
	im = Image.open('image.jpeg');
	im = array(im); #讲image转数组
	im1 = tools.imtools.imresize(im,[400,200]);
	imshow(im1);
	show();
	pass

#图片均衡化，使的黑的地方也能显示
def test3():
	im = array(Image.open('image2.jpg').convert('L'));
	im2,cdf = tools.imtools.histeq(im);
	#print im2
	#新建一个图像
	figure();
	im2 = Image.fromarray(im2)
	#im2.save('image_histeq.jpeg');
	#im1 = Image.fromarray(im)
	imshow(im2);
	show();

	# 显示直方图
	#hist(im.flatten(),128);
	#show();
	pass

# 高斯模糊图像，gaussian_filter第二个参数越大，模糊程度越高
def test4():
	im = array(Image.open('image.jpeg').convert('L'));
	im2 = filters.gaussian_filter(im,20);
	im2 = Image.fromarray(im2)
	im2.save('image_gaussian.jpeg');
	pass;

# 对颜色通道进行高斯模糊
def test5():
	im = array(Image.open('image.jpeg'));
	im2 = zeros(im.shape);
	for i in range(3):
		im2[:,:,i] = filters.gaussian_filter(im[:,:,i],20);
	im2 = uint8(im2);
	im2 = Image.fromarray(im2)
	im2.save('image_gaussian1.jpeg');
	pass;

if __name__ == "__main__":
	test5();