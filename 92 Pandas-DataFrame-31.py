# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:13:32 2020
合并数据 concat append() 用concat()和append()合并数据
@author: kanwa
"""

import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
scores2018_2 = excelDataset[list(excelDataset.keys())[2]]
courseInfo = excelDataset[list(excelDataset.keys())[3]]
studentsInfo = excelDataset[list(excelDataset.keys())[4]]
# concat数据集的添加,确保字段名字一样
scores2018_2 = scores2018_2.rename(columns={'studentsOfScores':'Scores'})
pd.concat(([scores2018_1,scores2018_2]))
scores2018_all1 = pd.concat([scores2018_1,scores2018_2])
scores2018_all2 = pd.concat([scores2018_1,scores2018_2],keys=[0,1])
scores2018_all3 = pd.concat([scores2018_1,scores2018_2],keys=['2018_Spring','2018_Autumn'])
scores2018_spring = scores2018_all3.loc['2018_Spring']
scores2018_autumn = scores2018_all3.loc['2018_Autumn']
cond1 = scores2018_all3['CourseID']=='Stat 321'
scores2018_all3[cond1]
scores2018_all3.reset_index(inplace=True)
scores2018_all3.columns
scores2018_all3.drop(columns=['level_1'],inplace=True)
scores2018_all3.columns
scores2018_all3.columns = ['Semester', 'CourseID', 'StudentID', 'Scores']
scores2018_all3.set_index(keys= ['Semester','CourseID','StudentID'],inplace=True)
scores2018_all3.index
scores2018_all3.loc[('2018_Spring')]
scores2018_all3.loc[('2018_Spring','Math 311')]
scores2018_all3.loc[('2018_Spring','Math 311','S2018002')]
# 重建索引，检索单个学生信息
scores2018_all3.reset_index(inplace=True)
scores2018_all3.set_index(keys= ['StudentID'],inplace=True)
scores2018_all3.loc['S2018002']
# append() method添加
scores2018_all4 = scores2018_1.append([scores2018_2])
# 合并列
scores2018_1_1 = scores2018_1.drop(columns=['CourseID'])
scores2018_1_2 = scores2018_1.drop(columns=['StudentID','Scores'])
scores2018_1_conat = pd.concat([scores2018_1_1,scores2018_1_2],axis=1)
