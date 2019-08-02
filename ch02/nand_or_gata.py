# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-21 12:51:35
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-21 13:38:25

import numpy as np

def NAND(x1,x2):
	x = np.array([x1,x2])
	w = np.array([-0.5,-0.5])
	b = 0.7

	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1

def OR(x1,x2):
	x = np.array([x1,x2])
	w = np.array([0.5,0.5])
	b = -0.2

	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1

if __name__ == '__main__':
	print("0 NAND 1 = " + str(NAND(0,1)))
	print("1 NAND 1 = " + str(NAND(1,1)))
	print("0 OR 0 = " + str(OR(0,0)))
	print("1 OR 1 = " + str(OR(1,1)))