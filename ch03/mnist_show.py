# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-29 11:34:10
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-31 09:45:12


import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
	pil_img = Image.fromarray(np.uint8(img))
	pil_img.show()


(x_trian,t_train),(x_test,t_test) = load_mnist(normalize=False, flatten=True)
img = x_trian[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28,28)
print(img.shape)
img_show(img)