# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:18:01 2020
画散点图和直方图
@author: andrew
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


# standard normal标准正态分布   mu=0 sigma=1
x = np.random.randn(500)
# sigma * np.random.randn(...) + mu
# Z=(X-mu)/sigma ~ N(0,1)
# X = Z*sigma+mu    ~Normal(mu,sigma)

# scatter 散点图
# figsize设置图片的尺寸 figsize=(10,10)
plt.figure(figsize=(10,10))
plt.subplot(211)
plt.plot(x,'.')
plt.subplot(212)
# 设置横轴与纵轴的尺寸
plt.xlim(left=0,right=500)
plt.ylim(top=3.2,bottom=-4)
plt.scatter(np.arange(len(x)),x)

# 直方图 横轴是数据，纵轴是出现的次数（也就是频数）
plt.figure(figsize=(10,10))
# bins就是箱子或者柱子的个数，可以省略，系统自动设置
plt.hist(x,bins=25)
# 有返回值
# n返回的是频数,bins是每个柱形的边界数值，patches是每个柱形对向的集合
n, bins, patches = plt.hist(x)

