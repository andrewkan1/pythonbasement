# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:51:53 2020
merge()之outer 外连接
@author: kanwa
"""

import pandas as pd

excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
scores2018_2 = excelDataset[list(excelDataset.keys())[2]]
courseInfo = excelDataset[list(excelDataset.keys())[3]]


# merge()之outer 或 inner 与 
scores2018_outer_course_scores = courseInfo.merge(scores2018_1,how='outer',on='CourseID')
# scores2018_inner_course_scores = courseInfo.merge(scores2018_1,how='inner',on='CourseID')

# scores2018_1与scores2018_2 merge with outer on='CourseID' ，CourseID没有交集
scores2018_outer_scores_scores_1 = scores2018_1.merge(scores2018_2,how='outer',on='CourseID')
# 增加一条记录，CourseID有交集
new_row = {'CourseID':'Math 311','StudentID':'S20180016','studentsOfScores':100}
scores2018_2_1 = scores2018_2.append(new_row, ignore_index=True)
scores2018_outer_scores_scores_2 = scores2018_1.merge(scores2018_2_1,how='outer',
                                                      on='CourseID',suffixes =['2018_Spring','2018_Autumn'])

# scores2018_1与scores2018_2 merge with outer on='StudentID' ，StudentID有交集 一对一
scores2018_outer_scores_scores_3 = scores2018_1.merge(scores2018_2_1,how='outer',
                                                      on='StudentID',suffixes =['2018_Spring','2018_Autumn'])
# 增加一条记录 'StudentID':'S2018001' 一对多
new_row = {'CourseID':'IT 121','StudentID':'S2018001','studentsOfScores':100}
scores2018_2_1 = scores2018_2_1.append(new_row, ignore_index=True)
scores2018_2_1.sort_values('StudentID',inplace=True)
scores2018_outer_scores_scores_4 = scores2018_1.merge(scores2018_2_1,how='outer',
                                                      on='StudentID',suffixes =['2018_Spring','2018_Autumn'])
# 增加一条记录 'StudentID':'S2018001' 多对多
new_row = {'CourseID':'Math 322','StudentID':'S2018001','Scores':100}
scores2018_1_1 = scores2018_1.append(new_row, ignore_index=True)
scores2018_1_1.sort_values('StudentID',inplace=True)
scores2018_outer_scores_scores_5 = scores2018_1_1.merge(scores2018_2_1,how='outer',
                                                      on='StudentID',suffixes =['2018_Spring','2018_Autumn'])