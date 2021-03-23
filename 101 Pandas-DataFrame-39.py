# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:31:04 2020
dataFrame中字符列的处理2
@author: kanwa
"""

import pandas as pd

excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
courseInfo = excelDataset[list(excelDataset.keys())[3]]


# 查找子字符串
courseInfo['CourseName']
new_row = {'CourseID':'Stat 323','CourseName':' Anvanced Theory of Probability 2 ','credits':3}
courseInfo = courseInfo.append(new_row, ignore_index=True)
cond1= courseInfo['CourseName'].str.contains('Probability')
courseInfocond1 = courseInfo[cond1]
#替代为：Probability&Statistics
replacestr = input('Please input Course Name:')
courseInfo['CourseName'] = courseInfo['CourseName'].str.replace('Probability',replacestr)

# Series.str 向量化字符串 ，举例计算同专业课程数量
s1 = courseInfo['CourseID'].str.split(' ')
s2 = s1.str.get(0)
stotal = s2.value_counts()
# 将以上三个语句合并
subjects = courseInfo['CourseID'].str.split(' ').str.get(0).value_counts()
# 然后将Series转换为dataframe
subjects = subjects.to_frame()
subjects.reset_index(inplace=True)


