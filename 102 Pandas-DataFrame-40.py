# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:43:00 2020
绘图1
@author: kanwa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 画一条直线，y轴的数值指定，x轴的数值matplotlib指定，从0开始[0,1,2,3]
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

plt.plot([1, 2, 3, 4],[1, 2, 3, 4])
plt.ylabel('some numbers')
plt.xlabel('some nmbers')
plt.show()
# axis()[x坐标最小值，x坐标最大值，y坐标最小值，y坐标最大值]
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

# sin函数
x = np.arange(0, 8, 0.1);
y = np.sin(x)
plt.plot(x, y)


# 举例
excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
scores2018_2 = excelDataset[list(excelDataset.keys())[2]]
plt.plot(scores2018_1['Scores'], 'ro')
plt.plot(scores2018_2['studentsOfScores'], 'g.')
plt.plot(scores2018_1['Scores'], 'r--')

# 课程平均成绩bar
subjectsScores = scores2018_1.groupby('CourseID')['Scores'].mean()
labels = list(subjectsScores.index)
plt.bar(labels,subjectsScores.values)
