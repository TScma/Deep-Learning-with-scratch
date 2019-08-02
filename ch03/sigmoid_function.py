# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-22 10:29:24
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-22 10:33:47

import numpy as np
import matplotlib.pyplot as plt

def sigmiod(x):
	return 1/(1+np.exp(-x))


x = np.arange(-5.0,5.0,0.1)
y = sigmiod(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()