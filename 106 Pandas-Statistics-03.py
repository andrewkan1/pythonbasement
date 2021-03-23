# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:45:18 2020
创建画板 生成图例 subplot legend
@author: Andrew
"""
import matplotlib.pyplot as plt
import numpy as np
# start:stop:step np.arrange()
Amp = 1 
freq= 1/2
phi = 0
t=np.r_[-5:5:0.1]

# y=Asin(wt+phi)=Asin(2*pi*f*t+phi) A是振幅Amplitude w是频率frequency phi是初始相位phase shift,
sinx = Amp * np.sin(2*np.pi*freq*t + phi)
cosx = Amp * np.cos(2*np.pi*freq*t + phi)
# plt.plot(t,cosx,color ='B',linewidth=2,label='COS',marker=".")
# plt.plot(t,sinx,color='R', linewidth=2,label='SIN',linestyle='--')

# Create a new figure创建一个新的图形
plt.figure()
# plt.subplot(211)
plt.subplot(121)
# get current axis 获得坐标轴对象
ax = plt.gca()                                            
# 将右、上的两条边颜色设置为空 
ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')         
# 指定下，左边分别为 x 轴和y 轴
ax.xaxis.set_ticks_position('bottom')   
ax.yaxis.set_ticks_position('left')          
#设置原点 data  设置的bottom，left(也就是x轴和y轴)的原点的0这个点上
ax.spines['bottom'].set_position(('data', 0))   
ax.spines['left'].set_position(('data', 0))
plt.plot(t,cosx,color ='B',linewidth=2,label='COS',marker=".")
plt.legend(loc ="upper right") 

# 第二个图形
# plt.subplot(212)
plt.subplot(122)
plt.plot(t,sinx,color='R', linewidth=1,label='SIN',linestyle='-')
plt.legend(loc ="lower left") 
# 保存
plt.savefig('my.jpg')
plt.show()