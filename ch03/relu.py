# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-22 13:07:10
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-22 13:09:21

import numpy as np
import matplotlib.pyplot as plt


def relu(x):
	return np.maximum(0,x)


x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()