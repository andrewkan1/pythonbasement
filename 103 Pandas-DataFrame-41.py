# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:03:50 2020
绘图2
@author: kanwa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data


excelDataset = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
scores2018_1 = excelDataset[list(excelDataset.keys())[1]]
scores2018_2 = excelDataset[list(excelDataset.keys())[2]]
scores2018_1.plot()
scores2018_2.plot()
scores2018_1.plot(x ='StudentID', y='Scores')

def score_performance(score):
    if score < 80:
        return "中等"
    elif score < 90:
        return '良好'
    else:
        return '优秀'
x = scores2018_1['Scores'].apply(score_performance)
rank = scores2018_1['Scores'].apply(score_performance).value_counts()
# 图例显示中文
plt.rcParams['font.sans-serif']=['SimHei'] 
rank.plot(kind='line')
scores2018_1['Scores'].apply(score_performance).value_counts().plot(kind='bar')
scores2018_1['Scores'].apply(score_performance).value_counts().plot(kind='barh')


# 从Internet读入股市数据
company ="MSFT"
start = '2019-06-01'
end = '2019-10-30'
stocks = data.DataReader(name = 'GOOG',data_source = 'yahoo',start = start, end = end)
stocks.plot()
stocks['High'].plot()
stocks.plot(y = 'High')
stocks['Close'].plot()
stocks[['High','Low']].plot()
# 修改画板 modifying Aesthetics
plt.style.available #templete 可用
plt.style.use('fivethirtyeight')
stocks['High'].plot()
plt.style.use('dark_background')
stocks.plot(y = 'Close')
plt.style.use('ggplot')
stocks.plot(y = ['High','Low'])
