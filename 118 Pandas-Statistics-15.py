# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:01:15 2020
 Population and Sample Standard deviation 
@author: andrew
"""

# numpy.std() 求标准差的时候默认是除以 n 的，即是有偏的，np.std无偏样本标准差方式为加入参数 ddof = 1
# pandas.std() 默认是除以n-1 的，即是无偏的，如果想有偏，需要加上参数ddof=0 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 

xval = np.arange(1,11)

randomdata = np.random.randn(10)
meanofdata = np.mean(randomdata)
# Population std 总体差
stdofdata1 = np.std(randomdata)
stdofdata2 = pd.DataFrame(randomdata).std(ddof=0)
# Sample std 样本差
stdofdata3 = np.std(randomdata,ddof=1)
stdofdata4 = pd.DataFrame(randomdata).std()
xval = xval
yval = randomdata
yerr = np.repeat(stdofdata2,len(randomdata))
# 标准差
x = np.linspace(0, 10, 1000)
y = np.repeat(meanofdata, 1000)
fig, ax1 = plt.subplots(1, 1,figsize=(10, 10))
# ax1.hist(groupdataframe['count'])
ax1.errorbar(xval, yval,  yerr = yerr,fmt='o',ecolor='Red',capsize=2) 
ax1.plot(x,y)
plt.show()

