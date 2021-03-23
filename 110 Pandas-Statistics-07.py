# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:21:09 2020
误差条图
@author: kanwa
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns  #需要安装该模块



employees = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesMaleSalary = employees[employees['Gender']=='Male']['Salary']
employeesFemaleSalary = employees[employees['Gender']=='Female']['Salary']

# employeesMaleSalary += 120000

employeesMaleSalary_mean = np.mean(employeesMaleSalary)
employeesFemaleSalary_mean = np.mean(employeesFemaleSalary)

employeesMaleSalary_std = np.std(employeesMaleSalary)
employeesFemaleSalary_std = np.std(employeesFemaleSalary)
labels =['employeesMaleSalary_mean','employeesFemaleSalary_mean']
employeesmeans = [employeesMaleSalary_mean,employeesFemaleSalary_mean]
employeesstds = [employeesMaleSalary_std,employeesFemaleSalary_std]

fig, ax = plt.subplots()
# ax.figure()
ax.bar(np.arange(len(employeesmeans)), employeesmeans,
       yerr=employeesstds,
       align='center',
       alpha=0.5,
       ecolor='red',
       capsize=10)
ax.yaxis.grid(True)
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(labels)
plt.tight_layout()
plt.show()


# employeesMaleSalary[0] = 199999
''' Standard Deviation 
Knowing whether SD error bars overlap or not does not let you conclude whether 
difference between the means is statistically significant or not.
'''
'''  Standard Error of the Mean
If two SEM error bars do overlap, and the sample sizes are equal or nearly equal, 
then you know that the P value is (much) greater than 0.05, so the difference 
is not statistically significant. The opposite rule does not apply. 
If two SEM error bars do not overlap, the P value could be less than 0.05, 
or it could be greater than 0.05. If the sample sizes  are very different, 
this rule of thumb does not always work.
'''
