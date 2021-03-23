# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:33:56 2020

@author: kanwa
根据字段的值返回所需要最大的或最小的几行数据
nlargest() nsmallest()
"""

import pandas as pd
import numpy as np


#读取csv
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo.info()
employeesInfo.head(n=5)
#根据字段的值返回所需要最大的或最小的几行数据
employeeInfoSalarymax1 = employeesInfo.nlargest(3,columns='Salary')
employeesInfo.sort_values('Salary',ascending = False, inplace = True)
employeeInfoSalarymin2 = employeesInfo.nsmallest(3,columns='Salary')
#对'Team'和'Salary'字段同时排序，team是object类型不能比较大小
employeeInfoSalarymin3 = employeesInfo.nlargest(3,columns=['Team','Salary'])
# category类型也不能比较大小
employeesInfo['Team'] = employeesInfo['Team'].astype('category')
employeeInfoSalarymin3 = employeesInfo.nlargest(3,columns=['Team','Salary'])
#对team先进行分类，然后编码
employeesInfo['Teamcode'] = employeesInfo['Team'].astype('category').cat.codes
employeeInfoSalarymax3 = employeesInfo.nlargest(10,columns=['Teamcode','Salary'])
employeeInfoSalarymax31 = employeesInfo.nlargest(3,columns=['Teamcode','Salary'])
# 如果有重复值，可用keep参数
employeeInfoSalarymax4 = employeesInfo.nlargest(10,columns=['Teamcode','Salary'],keep = 'all')
employeeInfoSalarymax5 = employeesInfo.nlargest(10,columns=['Teamcode','Salary'],keep = 'first')
employeeInfoSalarymax6 = employeesInfo.nlargest(10,columns=['Teamcode','Salary'],keep = 'last')
# Team字段中是'Sales'部门的员工的Salary最大4位
employeeInfoSalarymax7 = employeesInfo[employeesInfo['Team']=='Sales'].nlargest(4,columns='Salary')
employeeInfoSalarymax8 = employeesInfo[employeesInfo['Team']=='Sales'].sort_values('Salary', ascending=False).head(4)
