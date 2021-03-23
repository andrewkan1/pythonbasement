# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:01:48 2020
agg() 聚合方法 以及Groupby应用举例
agg() 聚合方法第88个视频
举例1         第89个视频
@author: kanwa
"""

import pandas as pd
import numpy as np

employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo['Team'].fillna(value='Internship',inplace = True)
employeesInfogroupmean = employeesInfo.groupby('Team').mean()
employeesInfogroupsum = employeesInfo.groupby('Team')['Salary'].sum()

# agg() 聚合方法
employeesInfogroupagg1 = employeesInfo.groupby('Team').agg('mean')
employeesInfogroupSalaryagg1 = employeesInfo.groupby('Team')\
['Salary'].agg(['mean','min','max','median','sum','std'])
employeesInfogroupSalaryagg2 = employeesInfo.groupby('Team')\
.agg({'Salary':['mean','median','std'],'Bonus %':['mean','max','min']})

# 依据已有Dataframe的结构，创建新的表格
# 同部门工资最高的员工
employeesInfonew = pd.DataFrame(columns = employeesInfo.columns) 
employeesInfoSortTeam = employeesInfo.sort_values(['Team','Salary'],ascending=[True,False])
# employeesInfogroupbyTeam = employeesInfo.groupby('Team') 
# https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html
for index, row in employeesInfo.groupby('Team'):
    # print(len(row))
    highestSalary = row.nlargest(1,'Salary')
    employeesInfonew.append(highestSalary)

# 举例1 创建Dummy变量，工资在前50%的是1，否则是0
employeesInfogroupstdsize = employeesInfo.groupby('Team').size().reset_index()
employeesInfo.sort_values(by=['Team','Salary'],ascending=[True,False],inplace=True)
employeesInfo['RankSize'] = employeesInfo.groupby('Team').cumcount()+1 
# 下面循环判断Team字段为空，Team是字符
for index, rowemployee in employeesInfo.iterrows():
    if rowemployee['Team'] !='':
        employeesInfo.loc[index,'GroupSize'] = \
            employeesInfogroupstdsize[employeesInfogroupstdsize["Team"]==rowemployee["Team"]][0].values
        
        
for index, rowemployee in employeesInfo.iterrows():
    if rowemployee['RankSize'] <= rowemployee['GroupSize'] * 0.5 :
        employeesInfo.loc[index,'DummySalarybyGroupSize'] = 1
    else:
        employeesInfo.loc[index,'DummySalarybyGroupSize'] = 0

# 举例同上 但是，如果Salary字段包含NaN，size()计数包括NaN values, count()则不包括NaN:
employeesInfo.loc[33,'Salary'] = np.nan
employeesInfogroupstdcount = employeesInfo.groupby('Team').count()['Salary'].reset_index()


employeesInfo.sort_values(by=['Team','Salary'],ascending=[True,False],inplace=True)
employeesInfo['RankCount'] = employeesInfo.groupby('Team')['Salary'].cumcount()+1 
for index1, rowemployee in employeesInfo.iterrows():
    temp = employeesInfogroupstdcount[employeesInfogroupstdcount["Team"]==rowemployee["Team"]]["Salary"]
    employeesInfo.loc[index1,'GroupCount'] = temp.values
    
for index, rowemployee in employeesInfo.iterrows():
    if rowemployee['RankCount'] <= rowemployee['GroupCount']:
        if rowemployee['RankCount'] <= rowemployee['GroupCount'] * 0.5:
            employeesInfo.loc[index,'DummySalarybyGroupCount'] = 1
        else:
            employeesInfo.loc[index,'DummySalarybyGroupCount'] = 0
