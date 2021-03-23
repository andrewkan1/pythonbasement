# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:30:19 2020
merge()之left right 左连接与右连接 
@author: kanwa
"""

import pandas as pd

excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
scores2018_2 = excelDataset[list(excelDataset.keys())[2]]
courseInfo = excelDataset[list(excelDataset.keys())[3]]
studentsInfo = excelDataset[list(excelDataset.keys())[4]]
# merge()之left right 左连接与右连接  一对一
scores2018_inner_course_students = studentsInfo.merge(scores2018_2,how='inner',on='StudentID')
scores2018_left_course_students = studentsInfo.merge(scores2018_2,how='left',on='StudentID')
scores2018_right_course_students = studentsInfo.merge(scores2018_2,how='right',on='StudentID')
scores2018_right_course_students1 = scores2018_2.merge(studentsInfo,how='left',on='StudentID')

# 多对一举例
new_row = {'CourseID':'Math 311', 'StudentID':'S2018001','studentsOfScores':93}
scores2018_2_1 = scores2018_2.append(new_row, ignore_index=True)
scores2018_2_1.sort_values('StudentID',inplace = True)

scores2018_left_course_students_1 = studentsInfo.merge(scores2018_2_1,how='left',on='StudentID')
scores2018_left_course_students_2 = scores2018_2_1.merge(studentsInfo,how='left',on='StudentID')

# 多对多举例
new_row = {'StudentID':'S2018001'}
studentsInfo_1 = studentsInfo.append(new_row, ignore_index=True)
studentsInfo_1.sort_values('StudentID',inplace = True)
scores2018_left_course_students_3 = studentsInfo_1.merge(scores2018_2_1,how='left',on='StudentID')
