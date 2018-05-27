# -*- coding: utf-8 -*-
import os
# 返回目录中所有jpg图片列表
def get_imlist(path):
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]