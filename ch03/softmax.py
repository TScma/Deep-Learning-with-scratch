# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-29 11:20:09
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-29 11:28:34

import numpy as np


def softmax(a):
	c = np.max(a)
	exp_a = np.exp(a - c)
	sum_exp_a = np.sum(exp_a)
	y = exp_a / sum_exp_a
	return y

a = np.array([0.3,2.9,4.0])
y = softmax(a)
print(y)