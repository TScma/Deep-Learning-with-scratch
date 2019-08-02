# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-22 14:01:12
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-22 15:03:11


import numpy as np


def sigmoid(x):
	return 1/(1+np.exp(-x))


def sigma_function(x):
	return x


X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

print(X.shape)
print(W1.shape)
print(B1.shape)

A1 = np.dot(X,W1) + B1
Z1 = sigmoid(A1)

print(A1)
print(Z1)

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1,W2)+B2
Z2 = sigmoid(A2)

print(A2)
print(Z2)

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

print(Z2.shape)
print(W3.shape)
print(B3.shape)

A3 = np.dot(Z2,W3)+B3
Y = sigma_function(A3)

print(A3)
print(Y)
