# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:45:47 2020
join()  how{‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘left’
@author: kanwa
"""

import pandas as pd

excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
courseInfo = excelDataset[list(excelDataset.keys())[3]]
# left 建立索引
scores2018_leftmerge_courseInfo = scores2018_1.merge(courseInfo,how='left',on='CourseID')
scores2018_leftjoin_courseInfo = scores2018_1.join(courseInfo,on='CourseID')

scores2018_1.set_index('CourseID',inplace=True)
courseInfo.set_index('CourseID',inplace=True)
scores2018_leftjoin_courseInfo = scores2018_1.join(courseInfo,on='CourseID')

# right
scores2018_Rightmerge_courseInfo = scores2018_1.merge(courseInfo,how='right',on='CourseID')
scores2018_rightjoin_courseInfo = scores2018_1.join(courseInfo,how='right',on='CourseID')

# inner
scores2018_innermerge_courseInfo = scores2018_1.merge(courseInfo,how='inner',on='CourseID')
scores2018_innerjoin_courseInfo = scores2018_1.join(courseInfo,how='inner',on='CourseID')

# outer
scores2018_outermerge_courseInfo = scores2018_1.merge(courseInfo,how='outer',on='CourseID')
scores2018_outerjoin_courseInfo = scores2018_1.join(courseInfo,how='outer',on='CourseID')
