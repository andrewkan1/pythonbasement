# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:38:43 2020
boxplot 箱型图
@author: kanwa
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


dataset = pd.read_sas(r'.\data\food.sas7bdat')
income = dataset['income']*100
food_exp = dataset['food_exp']
data = [income, food_exp] 
fig = plt.figure(figsize =(7, 5)) 
# Creating axes instance add_axes新增子区域 left, bottom, width, height = 0, 0, 1,1 
ax = fig.add_axes([0,0,1,1]) 
# Creating plot 
bp = ax.boxplot(data)
#设置标签
# labels = ['Income','Expenditure of Food']
# bp = ax.boxplot(data,labels=labels) 
# 设置均值showmeans， 显示均值线 meanline=True
# bp = ax.boxplot(data,meanline=True,showmeans = True) 
# 水平放置vert=False
# bp = ax.boxplot(data,showmeans = True,vert=False) 
# 显示中位线的豁口notch=3
# bp = ax.boxplot(data,notch=2,meanline=True,showmeans = True,vert=False,labels=labels) 
# outlier异常值的显示符号 sym='+'
# bp = ax.boxplot(data,sym='+',meanline=True,showmeans = True,vert=False) 
# 异常值的颜色克形状
# green_diamond = dict(markerfacecolor='g', marker='D')
# bp = ax.boxplot(data,notch=3,meanline=True,
#                 showmeans = True,vert=False,flierprops=green_diamond)  

#设置颜色patch_artist=True，然后调用方法set_facecolor
# bp = ax.boxplot(data,patch_artist=True)
# colors = ['pink', 'lightblue']
# for patch, color in zip(bp['boxes'], colors):
#     patch.set_facecolor(color)

plt.show() 

# 举例
# data_normal1 = np.random.normal(200, 100, 200) 
# data_normal2 = np.random.normal(300, 250, 200) 
# data_normal3 = np.random.normal(400, 50, 200) 
# data = [data_normal1, data_normal2,data_normal3] 
# ax = fig.add_axes([0,0,1,1]) 
# bp = ax.boxplot(data,meanline=True,showmeans = True,notch=3)
# plt.show() 