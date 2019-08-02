# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-21 13:42:27
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-21 14:09:26

import numpy as np

def AND(x1,x2):
	x = np.array([x1,x2])
	w = np.array([0.5,0.5])
	b = -0.7
	tmp = np.sum(w*x) + b
	if tmp <= 0:
		return 0
	else:
		return 1


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


def XOR(x1,x2):
	s1 = NAND(x1, x2)
	s2 = OR(x1, x2)
	y = AND(s1, s2)
	return y

if __name__ == '__main__':
	print("0 xor 1 = " + str(XOR(0,1)))
	print("1 xor 1 = " + str(XOR(1,1)))
