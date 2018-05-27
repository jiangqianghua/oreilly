# -*- coding: utf-8 -*-
'''
 本demo主要介绍Matplotlib的一些常用操作
'''
from  PIL import Image
from pylab import *

# 绘制线条
def test():
	im = array(Image.open('image.jpeg'));
	# 绘制图像
	imshow(im);
	# 定义4个点（100，200）(100,500) (400,200) (400,500)
	x = [100,100,400,400];
	y = [200,500,200,500];
	#使用红色星星绘制点
	'''
	颜色：b 蓝色 g 绿色 r 红色 c 青色 m 品红 y 黄色 k 黑色 w 白色
	线性：－ 实线 －－ 虚线 ：点线
	标记：. 点 o圆圈 s正方形 ＊星形 ＋加好 x叉号
	组合使用 plot(x,y,‘ks:’) 黑色正方形点线绘制
	'''
	plot(x,y,'r*');
	# 连接前两个点
	plot(x[:2],y[:2]);
	#添加标题
	title('plotting');
	#不显示坐标
	axis('off');
	#弹出框显示图片
	show();

#显示轮廓
def test2():
	im = array(Image.open('image.jpeg').convert('L'));
	#新建一个图像
	figure();
	#不使用颜色信息
	gray();
	# 在原点左上角显示轮廓图
	contour(im,origin='image');
	axis('equal');
	axis('off');
	show();

#显示直方图
def test3():
	im = array(Image.open('image.jpeg'));
	#新建一个图像
	figure();
	#显示直方图
	hist(im.flatten(),128);
	show();

# 交互式标注
def test3():
	im = array(Image.open('image.jpeg'));
	#新建一个图像
	figure();
	imshow(im);
	print 'please click 3 points';
	# 获取三次点击的坐标保存在x组数中
	x = ginput(3);
	print 'you clicked:',x;
	show();
if __name__ == "__main__":
	test3()