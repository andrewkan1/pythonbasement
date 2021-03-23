# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:20:10 2020
iterrows() iteritems()遍历行遍历列
@author: kanwa
"""

import pandas as pd
import numpy as np


#读取csv
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo.info()
employeesInfo.head(n=5)

# 遍历列名
for each in employeesInfo:
    print(each)
    
# 遍历行 Iterate over DataFrame rows as (index, Series) pairs.
for index,eachrow in employeesInfo.iterrows():
    print(index,eachrow)
    print('Salary:',eachrow['Salary'])

# 遍历列 Iterate over (column name, Series) pairs.   
for columnName,columns in employeesInfo.iteritems():
    print(columnName)
    print(columns)

# 遍历行
for i in range(len(employeesInfo)):
    rowiloc = employeesInfo.iloc[i]
    print(rowiloc)
    print('Salary:',eachrow['Salary'])