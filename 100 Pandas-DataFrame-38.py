# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:19:36 2020
dataFrame中字符列的处理1
@author: kanwa
"""

import pandas as pd

excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
courseInfo = excelDataset[list(excelDataset.keys())[3]]
# title() upper() lower() 字符大小写
courseInfo["semester"] = courseInfo["semester"].str.title()
courseInfo["semester"] = courseInfo["semester"].str.upper()
courseInfo["semester"] = courseInfo["semester"].str.lower()

# 查找子字符串
courseInfo['CourseName']
new_row = {'CourseID':'Stat 323','CourseName':' Anvanced Theory of probability 2 ','credits':3}
courseInfo = courseInfo.append(new_row, ignore_index=True)
cond1= courseInfo['CourseName'].str.contains('Probability')
courseInfocond1 = courseInfo[cond1]

# 如果输入包含有空格
userstr = input('Please input Course Name:')
cond2= courseInfo['CourseName'].str.contains(userstr)
courseInfocond2 = courseInfo[cond2]

userstr = userstr.rstrip()
userstr = userstr.lstrip()
userstr = userstr.strip()
# 为了查找方便，字符串前后去空格，然后改为小写
userstr = input('Please input Course Name:')
cond3= courseInfo['CourseName'].str.strip().str.lower().str.contains(userstr.strip().lower())
courseInfocond3 = courseInfo[cond3]
