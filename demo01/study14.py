# -*- coding: utf-8 -*-
'''
 本demo主要介绍导数
'''
from  PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
from scipy.ndimage import measurements, morphology
# 导数
def test():
	#新建一个图像
	figure();
	im = array(Image.open('image.jpeg').convert('L'));
	#计算x方向的导
	imx = zeros(im.shape);
	filters.sobel(im,1,imx);

	#计算y方向的导
	imy = zeros(im.shape);
	filters.sobel(im,0,imy);
	
	# 计算梯度
	magnitude = sqrt(imx**2+imy**2);

	subplot(2,3,1);
	imx = Image.fromarray(imx)
	imshow(imx);

	subplot(2,3,2);
	imy = Image.fromarray(imy)
	imshow(imy);

	subplot(2,3,3);
	magnitude = Image.fromarray(magnitude)
	imshow(magnitude);
	show();
	pass;

def test2():
	figure();
	sigma = 5 ; # 标准差
	im = array(Image.open('image.jpeg').convert('L'));
	#计算x方向的导
	imx = zeros(im.shape);
	filters.gaussian_filter(im,(sigma,sigma),(0,1),imx);

	imy = zeros(im.shape);
	filters.gaussian_filter(im,(sigma,sigma),(1,0),imy);

	subplot(2,2,1);
	#imx = Image.fromarray(imx);
	imshow(imx);

	subplot(2,2,2);
	#imx = Image.fromarray(imx);
	imshow(imy);

	# 计算梯度
	magnitude = sqrt(imx**2+imy**2);


	subplot(2,2,3);
	#magnitude = Image.fromarray(magnitude);
	imshow(magnitude);
	show();

def test3():
	im = array(Image.open('image.jpeg').convert('L'));
	im = 1*(im<128);
	labels ,nbr_objects = measurements.label(im);
	#print "number of objects:",nbr_objects
	figure();
	im0 = Image.fromarray(labels);
	print im0;
	imshow(im0);
	show();
	pass;
if __name__ == "__main__":
	test3();