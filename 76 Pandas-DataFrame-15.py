# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:01:57 2020

@author: kanwa
pandas 深度复制
"""

import pandas as pd
import numpy as np


#读取csv
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo.info()
employeesInfo.head(n=5)

#深度复制 
# =是辅助只是对象的引用，不是独立的
employeesInfoassignment1 = employeesInfo
id(employeesInfoassignment1)
id(employeesInfo)
id(employeesInfoassignment1) == id(employeesInfo)
employeesInfo.set_index('Emp ID',inplace=True)
employeesInfoassignment2 = employeesInfo
id(employeesInfoassignment2)
id(employeesInfo)
id(employeesInfoassignment1) == id(employeesInfoassignment2)
employeesInfoassignment2 = employeesInfo
employeesInfoassignment2.loc[employeesInfoassignment2['Team'] == 'Sales',['Salary']] = 200000

employeesInfoSales = employeesInfo[employeesInfo['Team'] == 'Sales']
id(employeesInfoSales)
id(employeesInfo)
employeesInfoSales.reset_index(inplace=True)
employeesInfoSales.drop(['Emp ID'],axis=1,inplace = True)

employeesInfoassignment3 = employeesInfo[:]
id(employeesInfoassignment3) == id(employeesInfo)
employeesInfoassignment3.reset_index(inplace=True)
# DataFrame中的每一列也是对象，也是浅复制，无法用id函数测出来
employeesInfoSalary1 = employeesInfo["Salary"]
id(employeesInfoSalary1) == id(employeesInfo["Salary"])
employeesInfoSalary1[:] = 123
employeesInfo["Salary"] = 2

employeesInfoSalary1 = employeesInfo["Salary"][:]
id(employeesInfoSalary1) == id(employeesInfo["Salary"])
employeesInfoSalary1[:] = 321
employeesInfo["Salary"] = 0

# 用copy复制，是一个deepcopy功能,参数deep=True时缺省的
employeesInfocopy1 = employeesInfo.copy()
id(employeesInfocopy1)
id(employeesInfo)
id(employeesInfocopy1) == id(employeesInfo)
employeesInfocopy1["Salary"] = 999

employeesInfoSalarycopy = employeesInfo['Salary'].copy(deep=True)
id(employeesInfoSalarycopy) == id(employeesInfo)
employeesInfoSalarycopy[0:4] = 1234

employeesInfo.loc[:2020003,'Salary'] = 9999


