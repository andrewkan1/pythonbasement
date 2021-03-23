# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:11:07 2020
merge VS excel Vlookup 
@author: kanwa
"""


import pandas as pd

excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
courseInfo = excelDataset[list(excelDataset.keys())[3]]


# left 
courseInfo_new = courseInfo[['CourseID','CourseName']]
scores2018_leftmerge_courseInfo = scores2018_1.merge(courseInfo_new,how='left',on='CourseID')
