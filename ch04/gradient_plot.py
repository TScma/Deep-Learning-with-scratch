# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-08-05 16:10:16
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-08-05 17:18:38


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def f(x, y):
    return x ** 2 + y ** 2

x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                 cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
plt.show()