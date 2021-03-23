# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:05:30 2020
merge()
left_on and right_on parameters 左右表的合并关键字段名字不一样
左表是index，右表是column
左右表都是index
@author: kanwa
"""

import pandas as pd

excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
scores2018_2 = excelDataset[list(excelDataset.keys())[2]]
courseInfo = excelDataset[list(excelDataset.keys())[3]]
studentsInfo = excelDataset[list(excelDataset.keys())[4]]

# left_on and right_on parameters 左右表的合并关键字段名字不一样
scores2018_2.rename(columns={'StudentID':'Student__ID'},inplace=True)
scores2018_inner_students_scores = studentsInfo.merge(scores2018_2,how='inner',
                                                     left_on='StudentID',right_on='Student__ID')
#左表是index，右表是column
studentsInfoIndex = studentsInfo.set_index('StudentID')
studentsInfoIndex_left_scores2018_1 = studentsInfoIndex.merge(scores2018_1,how='left',
                                                              left_index = True,
                                                              right_on = 'StudentID')
# 左右表都是index
scores2018_1_Index = scores2018_1.set_index('StudentID')
studentsInfoIndex_left_scores2018_1_Index = studentsInfoIndex.merge(scores2018_1_Index,
                                                                    how='left',
                                                              left_index = True,
                                                              right_index = True)

#将四个表合并成为一张大表
scores2018_2.rename(columns={'studentsOfScores':'Scores','Student__ID':'StudentID'},inplace = True)
scores2018_all = pd.concat([scores2018_1,scores2018_2])
studentsInfo_scores = studentsInfo.merge(scores2018_all,how='inner',on='StudentID')
studentsInfo_scores_course = studentsInfo_scores.merge(courseInfo,how='inner',on='CourseID')
