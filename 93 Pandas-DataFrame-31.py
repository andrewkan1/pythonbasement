# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:40:05 2020
合并数据集 merge
@author: kanwa
"""

import pandas as pd

excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
scores2018_2 = excelDataset[list(excelDataset.keys())[2]]
courseInfo = excelDataset[list(excelDataset.keys())[3]]
studentsInfo = excelDataset[list(excelDataset.keys())[4]]

# 尝试字段名字不一样时，concat会怎么样，（增加一个字段）
scores2018_all = pd.concat([scores2018_1,scores2018_2])
# 尝试字段/列的长度不一样，concat列会怎么样
scores2018_1_1 = scores2018_1.drop(columns=['CourseID'])
scores2018_1_2 = scores2018_1.drop(columns=['StudentID','Scores'])
cond1 = scores2018_1_2['CourseID']=='Math 311'
scores2018_1_2 = scores2018_1_2[cond1]
scores2018_1_conat = pd.concat([scores2018_1_1,scores2018_1_2],axis=1)
# merge()之inner 内连接——多对一
scores2018_2 = scores2018_2.rename(columns={'studentsOfScores':'Scores'})
scores2018_all = pd.concat([scores2018_1,scores2018_2],keys=['2018_Spring','2018_Autumn'])
scores2018_all.reset_index(inplace=True)
scores2018_all.columns
scores2018_all.drop(columns=['level_1'],inplace=True)
scores2018_all.columns
scores2018_all.columns = ['Semester', 'CourseID', 'StudentID', 'Scores']
# scores2018_all与courseInfo内连接
# how ‘inner’，‘left’, ‘right’, ‘outer’
scores2018_all_inner_course = scores2018_all.merge(courseInfo,how='inner',on='CourseID')

# 多对多 sql 
new_row = {'CourseID':'Math 311', 'CourseName':'Duplicate','credits':3,
           'semester':'spring','Intruduction':'An introduction to linear algebra. Topics include matrices, vectors, vector spaces, linear transformations, eigenvalues and eigenvectors. Prerequisites: A grade of C or better in MATH 212.',
           'Prerequisite':'MATH 212','ScoreOfPrerequisite':'A B C'}
courseInfo1 = courseInfo.append(new_row, ignore_index=True)
scores2018_all_inner_course1 = scores2018_all.merge(courseInfo1,how='inner',on='CourseID')
