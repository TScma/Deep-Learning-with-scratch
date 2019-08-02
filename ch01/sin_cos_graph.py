# -*- coding: utf-8 -*-
# @Author: GPUChen
# @Date:   2019-07-20 19:48:17
# @Last Modified by:   GPUChen
# @Last Modified time: 2019-07-20 19:57:33

import numpy as np
import matplotlib.pyplot as plt

# 生成数据

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x,y1,label="sin")
plt.plot(x,y2,label="cos",linestyle="--")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()
