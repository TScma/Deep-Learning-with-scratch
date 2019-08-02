# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-22 13:19:33
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-22 13:22:35

import numpy as np


X = np.array([1,2])
print(X.shape)
W = np.array([[1,3,5],[2,4,6]])
print(W)
print(W.shape)
Y = np.dot(X,W)
print(Y)
print(Y.shape)