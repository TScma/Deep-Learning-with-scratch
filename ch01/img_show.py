# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-20 19:58:02
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-20 20:00:19

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("../dataset/lena.png")
plt.imshow(img)
plt.show()