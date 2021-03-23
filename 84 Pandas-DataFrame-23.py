# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:30:05 2020
交换索引swaplevel() method  转置 transpose()
@author: kanwa
"""

import pandas as pd


employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo['Team'].fillna(value='Internship',inplace = True)
employeesInfo.set_index(keys = ['Team','Emp ID'],inplace = True)
employeesInfo.sort_index(inplace = True)
employeesInfoInternship = employeesInfo.loc[('Internship')]
employeesInfo.reset_index(inplace = True)
employeesInfo.set_index(keys = ['Team','Gender'],inplace = True)
employeesInfo.sort_index(ascending = [False,True],inplace = True)
employeesInfoloc1 = employeesInfo.loc['Marketing']
employeesInfoloc2 = employeesInfo.loc[(('Marketing','Sales','Finance'),('Male')),['First Name','Salary']]

# 交换索引swaplevel() method
indexlevel0 = employeesInfo.index.get_level_values(0)
indexlevel1 = employeesInfo.index.get_level_values(1)
employeesInfoswaplevel = employeesInfo.swaplevel()
indexlevelswaplevel0 = employeesInfoswaplevel.index.get_level_values(0)
indexlevelswaplevel1 = employeesInfoswaplevel.index.get_level_values(1)
employeesInfo.swaplevel(0,1)
# 转置 transpose()
employeesInfotrans = employeesInfo.transpose()


