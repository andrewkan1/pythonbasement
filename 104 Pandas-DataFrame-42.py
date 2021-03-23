# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:45:18 2020
用Numpy和matplotlib绘图,改变坐标轴
@author: kanwa
"""
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
# start:stop:step np.arrange()
Amp = 1 
freq= 1/2
phi = 0
t=np.r_[-5:5:0.1]

# y=Asin(wt+phi)=Asin(2*pi*f*t+phi) A是振幅Amplitude w是频率frequency phi是初始相位phase shift,
sinx = Amp * np.sin(2*np.pi*freq*t + phi)
cosx = Amp * np.cos(2*np.pi*freq*t + phi)

plt.figure()
# plt.xlabel('X ')
# plt.ylabel('Y ')                                #设置坐标轴的文字标签
# get current axis 获得坐标轴对象
ax = plt.gca()                                            

ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边

ax.xaxis.set_ticks_position('bottom')   
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴

ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))




plt.plot(t,sinx,color='R', linewidth=2,label='SIN')
plt.plot(t,cosx,color ='B',linewidth=2,label='COS',marker="o")
plt.legend(loc ="upper right") 
plt.savefig('my.jpg')
plt.show()