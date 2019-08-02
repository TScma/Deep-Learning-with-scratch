# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-22 10:51:28
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-22 10:57:42

import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
	return np.array(x > 0,dtype=np.int)


def sigmoid_function(x):
	return 1/(1+np.exp(-x))

x = np.arange(-5.0,5.0,0.1)
y1 = step_function(x)
y2 = sigmoid_function(x)

plt.plot(x,y1,"--")
plt.plot(x,y2)
plt.ylim(-0.1,1.1)
plt.xlabel("x")
plt.ylabel("y")
plt.title('sig & step')
plt.legend()
plt.show()