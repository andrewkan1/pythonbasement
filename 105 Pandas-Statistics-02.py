# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:45:18 2020
用Numpy和matplotlib绘图 ,改变坐标轴
@author: kanwa
"""
import matplotlib.pyplot as plt
import numpy as np
# start:stop:step np.arrange()
Amp =0.5
freq= 1/4
phi = 0
t=np.r_[-5:5:0.1]

# y=Asin(wt+phi)=Asin(2*pi*f*t+phi) A是振幅Amplitude w是频率frequency phi是初始相位phase shift,
sinx = Amp * np.sin(2*np.pi*freq*t + phi)
cosx = Amp * np.cos(2*np.pi*freq*t + phi)
# plt.plot(t,sinx,color='R', linewidth=1,label='SIN',linestyle='-')

# get current axis 获得坐标轴对象
ax = plt.gca()                                            

# 将右、上的两条边颜色设置为空 
ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')         
# 指定下，左边分别为 x 轴和y 轴
# ax.xaxis.set_ticks_position('bottom')   
# ax.yaxis.set_ticks_position('left')          
# plt.plot(t,sinx,color='R', linewidth=1,label='SIN',linestyle='-')
#设置原点 data  设置的bottom，left(也就是x轴和y轴)的原点的0这个点上
ax.spines['bottom'].set_position(('data', 0))   
ax.spines['left'].set_position(('data', 0))
# plt.plot(t,sinx,color='R', linewidth=1,label='SIN',linestyle='-')
ax.xaxis.label.set_text("X")                  # plt.xlabel('X')
ax.yaxis.label.set_text("Y")                  # plt.ylabel('Y')
# plt.plot(t,sinx,color='R', linewidth=1,label='SIN',linestyle='-')
# x y label的位置
ax.xaxis.set_label_coords(1,0.6)
ax.yaxis.set_label_coords(0.48,1)
# plt.plot(t,sinx,color='R', linewidth=1,label='SIN',linestyle='-')
# 将y轴标签旋转               
ax.set_ylabel('Y',rotation='horizontal')     # plt.ylabel('Y',rotation='horizontal')
# plt.plot(t,sinx,color='R', linewidth=1,label='SIN',linestyle='-')


# 绘图
plt.plot(t,sinx,color='R', linewidth=2,linestyle='-')
plt.plot(t,cosx,color ='B',linewidth=2,label='COS',marker="o")


plt.savefig('my.jpg')
plt.show()