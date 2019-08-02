# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-22 10:24:01
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-22 10:28:40


import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
	y = x > 0
	return y.astype(np.int)


x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()