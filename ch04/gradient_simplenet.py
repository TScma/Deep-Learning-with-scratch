# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-08-13 11:04:45
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-08-13 11:54:19

import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.function import softmax,cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:
	"""docstring for simpleNet"""
	def __init__(self):
		self.W = np.random.randn(2,3)

	def predict(self,x):
		return np.dot(x,self.W)
	
	def loss(self,x,t):
		z = self.predict(x)
		y = softmax(z)
		loss = cross_entropy_error(y,t)

		return loss


t = np.array([0,0,1])

net = simpleNet()
print(net.W)

x = np.array([0.6,0.9])
p = net.predict(x)
print(p)

f = lambda w:net.loss(x,t)
dw = numerical_gradient(f,net.W)

print(dw)
