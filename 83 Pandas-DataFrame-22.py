# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:58:50 2020
MultiIndex多重索引
@author: kanwa
"""

import pandas as pd


employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo['Team'].fillna(value='Internship',inplace = True)
employeesInfo.set_index('Team',inplace = True)
employeesInfo.reset_index(inplace=True)
employeesInfo.set_index(keys = ['Team','Emp ID'],inplace = True)
employeesInfo.sort_index(inplace = True)
employeesInfo.index
employeesInfo.index[0]
employeesInfo.index[0][1]
employeesInfo.index[0][0]

# get_level_values()对于多级索引取值
indexlevel0 = employeesInfo.index.get_level_values(0)
indexlevel1 = employeesInfo.index.get_level_values(1)
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv',index_col=['Team','Emp ID'])
employeesInfo.reset_index(inplace=True)
employeesInfo['Team'].fillna(value='Internship',inplace = True)
employeesInfo.set_index(keys = ['Team','Emp ID'],inplace = True)
indexlevel2 = employeesInfo.index.get_level_values(0)
indexlevelTeam = employeesInfo.index.get_level_values('Team')
indexlevel3 = employeesInfo.index.get_level_values(1)
indexlevelEmpID = employeesInfo.index.get_level_values('Emp ID')
# set_name 将多个索引重新命名
employeesInfo.index.set_names(['Department','ID of Employees'],inplace = True)

# sort_index()
employeesInfo.sort_index(ascending = True,inplace = True)
employeesInfo.sort_index( ascending = False,inplace = True)
# 第一索引降序第二索引升序
employeesInfo.sort_index(ascending = [False,True],inplace = True)
employeesInfoInternship = employeesInfo.loc[('Internship')]

