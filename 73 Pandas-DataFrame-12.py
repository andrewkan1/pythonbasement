# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:51:51 2020

@author: kanwa
用drop()删除数据,用sample()随机取样
"""

import pandas as pd
import numpy as np


#读取csv
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo.info()
# 用drop()删除行或列的数据
# 删除行的数据
employeesInfo.drop(0,inplace = True)
employeesInfo.drop(73,inplace = True)
# 删除列的数据
employeesInfo.drop('Emp ID',axis = 1,inplace = True)
employeesinfoDelcolumns1 = employeesInfo.drop(columns =['Last Login Time','Last Name'])
employeesinfoDelcolumns2 = employeesInfo.pop('Last Login Time')
del employeesInfo['Last Name']
# 以索引为依据删除数据
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo.sort_values('First Name',inplace = True)
employeesInfo.set_index('First Name',inplace = True)
employeesinfoDelrowscolumns1 = employeesInfo.drop(index =['Ann','Anne'])
employeesinfoDelrowscolumns2 = employeesInfo.drop(index =['Ann','Anne'],columns =['Last Login Time','Last Name'])
# 随机取样sample
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfoSample1 = employeesInfo.sample(n=3)
employeesInfoSample2 = employeesInfo.sample(frac=0.25)
employeesInfoSample3 = employeesInfo.sample(frac=0.30,axis = 1) 
employeesInfoSample4 = employeesInfo['Salary'].sample(frac=0.30) 
