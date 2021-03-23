# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:40:58 2020
累积频率 CDF(cumulative density function)的计算以及绘图
@author: andrew
"""

# PDF(probability density function ) 


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns  



x = [1, 4, 2, 1, 3, 1,6,7]
res = stats.cumfreq(x)
# res = stats.cumfreq(x,numbins=10, defaultreallimits=(1.5, 10))
# 第一个柱形中心起始点
res.lowerlimit
# 柱形的宽度
res.binsize
# 柱形的高度（X中的数值有多少个会积累落入该柱形中，也就是说，当前柱形X中的值落入当前柱形中的数量加上以前的数值）
res.cumcount
x1 = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size,res.cumcount.size)

plt.figure(figsize=(10,10))
plt.subplot(411)
plt.bar(x1, res.cumcount, width=res.binsize,align='center')
plt.subplot(412)
plt.plot(res[0])
plt.subplot(413)
# n
n, bins, patches = plt.hist(x) 
plt.subplot(414)
sns.kdeplot(x)



GPDDataset = pd.read_csv(r'.\data\GPDcsvData.csv')
plt.figure(figsize=(7,7))
plt.subplot(141)
n, bins, patches = plt.hist(GPDDataset['gdpPerCapita'])
plt.subplot(142)
sns.kdeplot(GPDDataset['gdpPerCapita'])
plt.subplot(143)
cdf = stats.cumfreq(GPDDataset['gdpPerCapita'])
# plt.plot(cdf[0])

xCoordinate = cdf.lowerlimit + np.linspace(0, cdf.binsize*cdf.cumcount.size,cdf.cumcount.size)
plt.bar(xCoordinate, cdf.cumcount, width=res.binsize,align='center')

plt.plot(cdf[0])

plt.subplot(144)
# np.histogram计算直方图的频次但是不画图
hist, bin_edges = np.histogram(GPDDataset['gdpPerCapita'])
cdf = np.cumsum(n)
plt.plot(cdf)
plt.show()