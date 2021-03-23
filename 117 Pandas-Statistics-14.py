# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:14:19 2020

@author: kanwa
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

dataset = pd.read_sas(r'.\data\food.sas7bdat')
income = dataset['income']*100
income = income.to_frame()
groupdataframe = pd.DataFrame(columns = ['LowerExpenditure', 'UpperExpenditure', 'count'])
labels = []
# 将income中的数值分组，然后计数
for i in range(7):
    labels.append(str(i*500)+'_'+str((i+1)*500))
    LowerExpenditure = i * 500
    UpperExpenditure = (i+1) * 500
    cond1 = income['income'] >= LowerExpenditure
    cond2 = income['income'] < UpperExpenditure
    cond = cond1 & cond2
    count = income[cond].count()[0]
    groupdataframe = groupdataframe.append(pd.DataFrame({'LowerExpenditure':[LowerExpenditure],
                                   'UpperExpenditure':[UpperExpenditure],
                                   'count':[count]}),ignore_index=True)

sumofgroup =0

for index,eachrow in groupdataframe.iterrows():
    midpoint = (eachrow['LowerExpenditure'] + eachrow['UpperExpenditure'])/2
    sumofgroup += midpoint * eachrow['count']
meanofgroup = sumofgroup/groupdataframe['count'].values.sum()
 
fig, ax1 = plt.subplots(1, 1,figsize=(10, 10))
# ax1.hist(groupdataframe['count'])
ax1.bar(labels,groupdataframe['count'])
plt.show()