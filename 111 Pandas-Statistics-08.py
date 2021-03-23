# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:21:09 2020
误差条图 errorbar
@author: andrew
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns  #需要安装该模块



xval = np.arange(0.1, 4, 0.5) 
# Calculate the exponential of all elements in the input array
yval = np.exp(-xval) 
plt.plot(xval,yval,label ='Line1')  
plt.legend(loc ='upper right') 
plt.show()


yerrlist = [0.1, 0.2,0.5,0.4,0.3,0.3,0.9,1 ]
plt.errorbar(xval, yval,  yerr = 0.5) 
plt.errorbar(xval, yval,  yerr = 0.5,fmt='o') 
plt.errorbar(xval, yval,  yerr = yerrlist,fmt='o') 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o') 
# matplotlib.pyplot.errorbar(x, y, yerr=None, xerr=None, fmt='', ecolor=None, 
#                            elinewidth=None, capsize=None, barsabove=False, 
#                            lolims=False, uplims=False, xlolims=False, 
#                            xuplims=False, errorevery=1, capthick=None, 
#                            *, data=None, **kwargs)[source]
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red') 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red',capsize=3) 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red',
             elinewidth=3,capsize=3,capthick=2) 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red',
             elinewidth=3,capsize=3,capthick=2,barsabove=True) 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red',
             elinewidth=3,capsize=3,capthick=2,errorevery=3) 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red',
             elinewidth=3,capsize=3,capthick=2,lolims=True) 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red',
             elinewidth=3,capsize=3,capthick=2,lolims=True,uplims=True) 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red',
             elinewidth=3,capsize=3,capthick=2,lolims=True,uplims=True,xlolims=True) 
plt.errorbar(xval, yval,  xerr = 0.4, yerr = yerrlist,fmt='o',ecolor='Red',
             elinewidth=3,capsize=3,capthick=2,lolims=True,uplims=True,xlolims=True,xuplims=True) 
plt.errorbar(xval+1, yval+1, xerr = 0.4, yerr = 0.5,label ='Line1',barsabove=False,capsize=5) 
plt.legend(loc ='upper left') 
plt.show()

