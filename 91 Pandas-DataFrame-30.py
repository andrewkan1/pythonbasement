# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:30:23 2020
保存dataframe到文件,自动生成变量
@author: kanwa
"""

import pandas as pd

studentsInfo1 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = ['ScoresOfStudents2018Spring','Sheet1'])
studentsInfo2 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)

# 自动生成变量
studentsInfo2.keys()
studentsInfo2.values()
list(studentsInfo2.keys())
len(studentsInfo2 )
studentsInfo2sheet1 = studentsInfo2['Sheet1']

studentsInfo2sheet1 = studentsInfo2[list(studentsInfo2.keys())[0]]
studentsInfo2sheet2 = studentsInfo2[list(studentsInfo2.keys())[1]]
studentsInfo2sheet3 = studentsInfo2[list(studentsInfo2.keys())[2]]
studentsInfo2sheet4 = studentsInfo2[list(studentsInfo2.keys())[3]]
studentsInfo2sheet5 = studentsInfo2[list(studentsInfo2.keys())[4]]
 
for i in range(0,len(studentsInfo2)):
    exec("studentsInfo2_sheet%d = studentsInfo2[list(studentsInfo2.keys())[%d]]" % (i+1,i))
# 数据的值一样，但是数据的类型不一样
studentsScores1 = studentsInfo2sheet1["Scores"]
studentsScores2 = studentsInfo2sheet1["Scores"].to_list()
studentsScores3 = studentsInfo2sheet1["Scores"].to_frame()
# 保存dataframe到文件
studentsScores3.to_excel('.\data\studentsScores.xlsx')
studentsScores3.to_csv('.\data\studentsScores.csv')
with pd.ExcelWriter('.\data\studentsScores.xlsx') as writer:
    studentsScores3.to_excel(writer,sheet_name = 'Scores1')
    studentsInfo2sheet1.to_excel(writer,sheet_name = 'StudentsInfo')
    writer.save()