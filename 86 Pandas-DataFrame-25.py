# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:06:47 2020
数据透视表pivot() , pivot_table() and melt()
@author: kanwa
"""

import pandas as pd
studentsScores = pd.read_excel(r'.\data\ScoresofStudents.xlsx')
studentsScoresRank = studentsScores.sort_values(['TestID','Scores'],ascending=[True,False])
studentsScoresRank['Rank'] = studentsScoresRank.groupby('TestID').cumcount()+1


# pivot()侧重于reshape,就是构建一个结构可能不同的新的dataframe
# 所以在行与列的交叉点值的索引应该是唯一值，否则出错，合并同类项
# 可以将index当做行，columns当做列
studentsScorespivot = studentsScores.pivot(index='TestID', columns='Name', values='Scores')
studentsScorespivottrans = studentsScorespivot.transpose()
studentsScorespivotnew = studentsScores.pivot(index='Name', columns='TestID', values='Scores')

studentsScoresRankpivot = studentsScoresRank.pivot(index='TestID', columns='Name')
print(studentsScoresRankpivot.columns)
studentsScoresRankpivot.info()
studentsScoresRankpivottrans = studentsScoresRankpivot.transpose()
studentsScoresRankpivotnew = studentsScoresRank.pivot(index='Name', columns='TestID')

# pivot_table()数据透视表
studentsScores1 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx')
# studentsScoresRank1 = studentsScores1.sort_values(['TestID','Scores'],ascending=False)
# studentsScoresRank1['Rank'] = studentsScoresRank1.groupby('TestID').cumcount()+1
# pivot()以下会出错误
# studentsScorespivot1 = studentsScores1.pivot(index='TestID', columns='Name', values='Scores')
# pivot_table(), aggfunc = 'mean'
studentsScorespivot1 = studentsScores1.pivot_table(index='TestID', columns='Name', values='Scores')
studentsScorespivot2 = studentsScores1.pivot_table(index='TestID', columns='Name', values='Scores',aggfunc = 'mean')
studentsScorespivot3 = studentsScores1.pivot_table(index='TestID', columns='Name', values='Scores',aggfunc = 'sum')
studentsScorespivot4 = studentsScores1.pivot_table(index='TestID', columns='Name', values='Scores',aggfunc = 'median')
studentsScorespivot5 = studentsScores1.pivot_table(index='TestID', columns='Name', values='Scores',aggfunc = 'max')
studentsScorespivot6 = studentsScores1.pivot_table(index='TestID', columns='Name', values='Scores',aggfunc = 'min')
# 每一次考试的平均值，成绩中位数
studentsScorespivot7 = studentsScores1.pivot_table(index='TestID',  values='Scores',aggfunc = 'mean')
studentsScorespivot8 = studentsScores1.pivot_table(index='TestID',  values='Scores',aggfunc = 'median')
# 每一位学生的平均成绩，成绩中位数
studentsScorespivot9 = studentsScores1.pivot_table(index='Name',  values='Scores',aggfunc = 'mean')
studentsScorespivo10 = studentsScores1.pivot_table(index='Name',  values='Scores',aggfunc = 'median')

# melt() pivot()的逆向操作，将宽数据变为长数据
studentsScorespivot.info()
studentsScorespivot.reset_index(inplace=True)
studentsScorespivotmelt = pd.melt(studentsScorespivot,id_vars = 'TestID')
studentsScorespivotmeltAnn = pd.melt(studentsScorespivot,id_vars = 'TestID',value_vars = 'Ann')
studentsScorespivotmeltAnnJohn = pd.melt(studentsScorespivot,id_vars = 'TestID',value_vars = ['Ann','John'])
studentsScorespivotmeltAnnJohn1 = pd.melt(studentsScorespivot,id_vars = 'TestID',var_name = 'First Name',value_vars = ['Ann','John'])

