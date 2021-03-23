# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:41:38 2020
核密度估计kdeplot 直方图举例 安装seaborn
@author: andrew
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns  #需要安装该模块



GPDDataset = pd.read_csv(r'.\data\GPDcsvData.csv')
fig, axes = plt.subplots(nrows=3, ncols=1,figsize=(15,15))
ax0,ax1,ax2 = axes.flatten()
ax0.scatter(np.arange(len(GPDDataset['gdpPerCapita'])),GPDDataset['gdpPerCapita'])
n, bins, patches = ax1.hist(GPDDataset['gdpPerCapita'])
ax2.hist([GPDDataset['imfGDP'],GPDDataset['unGDP']],label=['IMF','UN'])
ax2.legend(prop={'size': 10})
plt.show()

# 核密度估计
sns.kdeplot(GPDDataset['gdpPerCapita'])
(mu, sigma) = stats.norm.fit(GPDDataset['gdpPerCapita'])


x = np.random.randn(200)
plt.hist(x,bins=25)
sns.kdeplot(x)
(mu, sigma) = stats.norm.fit(x)
