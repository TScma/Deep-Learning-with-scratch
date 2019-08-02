# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-08-01 09:42:01
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-08-01 09:51:43

import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist


(X_train,t_train),(X_test,t_test) = load_mnist(normalize=True,one_hot_label=True)
print(X_train.shape)
print(t_train.shape)

train_size = X_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size,batch_size)
X_batch = X_train[batch_mask]
t_batch = t_train[batch_mask]


def cross_entropy_error(y,t):
	if y.ndim == 1:
		t = t.reshape(1,t.size)
		y = y.reshape(1,y.size)
	batch_size = y.shape[0]
	return -np.sum(“np.log(y[np.arange(batch_size), t] + 1e-7))/batch_size


