# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:12:29 2020
分组 groupby
@author: kanwa
"""
import pandas as pd

employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo['Team'].fillna(value='Internship',inplace = True)
# groupby不需要提前sort_values
employeesInfo.sort_values('Team',inplace=True)
employeesInfogroup = employeesInfo.groupby('Team').groups
employeesInfogroup['Marketing']
employeesInfogroup['Marketing'][1]
employeesInfogroupmean = employeesInfo.groupby('Team').mean()
employeesInfogroupmean = employeesInfo.groupby('Team')['Salary'].mean()
employeesInfogroupsum = employeesInfo.groupby('Team')['Salary'].sum()
employeesInfogroupmax = employeesInfo.groupby('Team')['Salary'].max()
employeesInfogroupmin = employeesInfo.groupby('Team')['Salary'].min()
employeesInfogroupmedian = employeesInfo.groupby('Team')['Salary'].median()
employeesInfogroupstd = employeesInfo.groupby('Team')['Salary'].std()
employeesInfogroupsize = employeesInfo.groupby('Team')['Salary'].size()
employeesInfo.groupby('Team')['Salary'].size().sum()
employeesInfogroup.mean()
employeesInfogroup = employeesInfo.groupby('Team')
employeesInfogroup.first
employeesInfogroup.last()
employeesInfo['Order'] = employeesInfo.groupby('Team').cumcount() 

# 举例 显示雇员工资数与本部门平均工资的差距
Salarygroupmean = employeesInfo.groupby('Team')['Salary'].mean().reset_index()

for index1, rowemployee in employeesInfo.iterrows():
    for index2, rowsalary in Salarygroupmean.iterrows():
        if rowemployee['Team'] == rowsalary['Team']:
            employeesInfo.loc[index1,'TeamSalaryMean1'] = rowsalary['Salary']
            
for index1, rowemployee in employeesInfo.iterrows():
    temp = Salarygroupmean[Salarygroupmean["Team"]==rowemployee["Team"]]['Salary']
    employeesInfo.loc[index1,'TeamSalaryMean2'] = temp.values

employeesInfo['differenceOfSalaryFromMean'] = employeesInfo['Salary'] - employeesInfo['TeamSalaryMean2'] 
