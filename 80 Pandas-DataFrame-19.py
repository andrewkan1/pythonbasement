# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:26:22 2020
pandas_datareader与.dt Accessor
@author: kanwa
"""

import pandas as pd
import datetime as dt

# .dt Accessor
timesperiod1 = pd.date_range(start ='2010-01-01',end = '2020-3-21',freq = '24D')
s = pd.Series(timesperiod1)
s.head()
sday = s.dt.day
s.dt.year
s.dt.quarter
s.dt.month
s.dt.week
s.dt.weekday_name
cond1 = s.dt.is_quarter_start
s[cond1]
cond2 = s.dt.is_quarter_end
s[cond2]
# 使用Python的pandas-datareader包下载雅虎财经股价数据
#  import Financial Data Set with pandas_datareader Library
from pandas_datareader import data
company ="MSFT"
start = '2019-01-01'
end = '2020-01-31'
stocks1 = data.DataReader(name = company,data_source = 'yahoo',start = start, end = end)
stocks1.values
stocks1.columns
stocks1.index
# 根据时间索引取值
stocks1.loc['2019-12-13']
stocks1.loc['2019-12-13']['High']
stocks1.loc['2019-12-13','High']
stocks1['High'].at['2019-12-13']
#取不到该值 因为星期日没有股市数据 stocks1.loc['2019-12-15']
stocks1.iloc[10]
stocks1['High'].iat[10]
stocksperiod1 = stocks1.loc['2019-02-02':'2019-04-15']
stocksperiod2 = stocks1.loc[pd.to_datetime(['2019-02-01','2019-04-15'])]

