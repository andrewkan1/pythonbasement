# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:18:21 2020

@author: kanwa
用where过滤数据 查询query() 自定义函数 apply() 
"""

import pandas as pd
import numpy as np


#读取csv
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo.info()
employeesInfo.head(n=5)
#用where过滤数据,不满足条件的记录不是删除，然是为Nan
employeesInfoSalary1 = employeesInfo.where(employeesInfo['Salary']>120000)
employeesInfoSalary2 = employeesInfo[employeesInfo['Salary']>120000]
employeesInfoSalary3 = employeesInfo.where(employeesInfo['Salary']>120000,other = '不满足条件')

# 查询query()   
employeesInfoquery5 = employeesInfo.query('Salary >120000 ')
employeesInfoquery6 = employeesInfo.query('Salary >120000 and Gender == "Female"')

#应用自定义函数 apply() 
def covert_to_dummy(gender):
    if gender == 'Male':
        return 0
    elif gender == 'Female':
        return 1
    else:
        return 0

employeesInfo['Gender'].apply(covert_to_dummy)
employeesInfo['Gender'] = employeesInfo['Gender'].apply(covert_to_dummy)

def SalaryRank(row):
    print(row)
    if row['Salary'] > 120000:
        return 'High'
    elif row['Salary'] > 80000:
        return 'Middle'
    elif row['Salary'] > 60000:
        return 'Mean'
    else:
        return 'Low'
    
    
employeesInfo.apply(SalaryRank,axis='columns')
employeesInfo['SalaryRank'] = employeesInfo.apply(SalaryRank,axis='columns')    
    

