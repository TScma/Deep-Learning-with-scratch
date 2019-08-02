# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-20 20:05:10
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-20 20:15:38

import numpy as np

def simple_perceptron(x1,x2):
	w1 ,w2 ,theta = 0.5,0.5,0.7
	tmp = w1*x1 + w2*x2
	if tmp <= theta:
		return 0
	else:
		return 1

def np_perception(x1,x2):
	x = np.array([x1,x2])
	w = np.array([0.5,0.5])
	b = -0.7
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1


if __name__ == '__main__':
	print(simple_perceptron(0,1))
	print(simple_perceptron(1,1))
	print(np_perception(0,1))
	print(np_perception(1,1))
