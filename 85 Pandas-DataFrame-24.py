# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:02:27 2020
stack()与unstack()方法 与转置transpose
@author: kanwa
"""

import pandas as pd


# stack()与unstack()方法
employeesInfo = pd.read_csv(r'.\data\employeesinfo.csv',index_col=['Team','Emp ID'])
employeesInfo.sort_index(ascending = [False,True],inplace = True)
employeesInfostack = employeesInfo.stack()
employeesInfostackframe = employeesInfo.stack().to_frame()
# 要确保索引唯一才能unstack
employeesInfounstack1 = employeesInfostack.unstack()
employeesInfounstack2 = employeesInfostack.unstack(level=['Emp ID'])
employeesInfounstack3 = employeesInfostack.unstack(level=['Team'])
employeesInfounstack4 = employeesInfostack.unstack(level=['Team','Emp ID'])
# 转置transpose
employeesInfotrans = employeesInfo.transpose()
# 举例 将行的数据转换成列的数据 类似于数据透视表
studentsScores = pd.read_excel(r'.\data\ScoresofStudents.xlsx')
studentsScores.set_index(keys=['TestID','Name'],inplace = True)
studentsScoresstack = studentsScores.stack()
studentsScoresunstack =studentsScores.unstack(level='TestID')

studentsScores = pd.read_excel(r'.\data\ScoresofStudents.xlsx')
studentsScoresRank = studentsScores.sort_values(['TestID','Scores'],ascending=False)
studentsScoresRank['Rank'] = studentsScoresRank.groupby('TestID').cumcount()+1
studentsScoresRankstack  = studentsScoresRank.stack()
# 每个学生每一次的考试成绩由多行转变为一行
studentsScoresRank.set_index(keys=['TestID','Name'],inplace = True)
studentsScoresRankunstack =studentsScoresRank.unstack(level=['TestID'])
studentsScoresT0001 = studentsScoresRankunstack.iloc[:,[0,3]]
studentsScoresT0001 = studentsScoresRankunstack[studentsScoresRankunstack.columns[[0,3]]]
# 修改列名
studentsScoresT0001.columns = ['ScoresT0001','RankT0001']
