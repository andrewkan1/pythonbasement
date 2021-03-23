# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:05:15 2020
数据分布的描述 均值 上 理论部分
@author: kanwa
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns  #需要安装该模块

data = np.arange(10)
mean = np.mean(data)
# 如何处理空值
# hstack vstack stack
data1= np.hstack((data,np.nan))        
mean1 = np.mean(data1)
mean2 = np.nanmean(data1)

# median 不受极值影响
median = np.median(data)
data2 = np.append(data,1000)
meanofdata2 = np.mean(data2)
medianofdata2 = np.median(data2)


fig, (ax1, ax2,ax3) = plt.subplots(3, 1,figsize=(17, 17))
ax1.hist(data2)
ax2.hist(data)
ax3.bar([1,2,3,4,5,6,7,8,9,10,11],data2)
plt.show()

# mode 提供众数的值和频数
datamode = [1,2,3,3,3,3,4,4,5,5,6,7]
mode = stats.mode(datamode)
mode[0][0]
mode[1][0]
fig, (ax1) = plt.subplots(1, 1)
# fig, (ax1, ax2) = plt.subplot(1, 2)
ax1.hist(datamode)
plt.show()

# geometric
datageometric = np.arange(1,11)
geomean = stats.gmean(datageometric)