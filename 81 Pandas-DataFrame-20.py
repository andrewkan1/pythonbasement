# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:47:58 2020
日期时间偏移量
@author: kanwa
"""
import pandas as pd
import datetime as dt
from pandas_datareader import data

# 日期时间偏移量对象 pd.Dateoffset Objects
stocksdata1 = data.DataReader(name = 'GOOG',data_source = 'yahoo',start = dt.date(2010,1,1), end = dt.datetime.now())
stocksdata2 = stocksdata1.copy()
stocksdata2.index = stocksdata1.index + pd.DateOffset(days = 5)
stocksdata2.index = stocksdata1.index + pd.DateOffset(weeks = 2)
stocksdata2.index = stocksdata1.index + pd.DateOffset(months = 1)
stocksdata2.index = stocksdata1.index + pd.DateOffset(hours = 3)
stocksdata2.index = stocksdata1.index + pd.DateOffset(years = 1 , months = 1, days =1)
stocksdata2.index = stocksdata1.index + pd.DateOffset(years = 1 , months = 1, days =1,hours = 1, minutes = 1, seconds = 2)

# 年，季度，月等的首尾日期
MydateOrigin = dt.datetime(2020, 1, 2, 10, 30)
Mydate1 = MydateOrigin + pd.tseries.offsets.MonthBegin()
Mydate2 = MydateOrigin - pd.tseries.offsets.MonthBegin()
Mydate3 = MydateOrigin + pd.tseries.offsets.MonthEnd()
Mydate4 = MydateOrigin - pd.tseries.offsets.MonthEnd()
from pandas.tseries.offsets import *
Mydate5 = MydateOrigin - BMonthBegin()
Mydate6 = MydateOrigin + BMonthBegin()
Mydate7 = MydateOrigin + BMonthEnd()
Mydate8 = MydateOrigin - BMonthEnd()
Mydate9 = MydateOrigin + QuarterEnd()
Mydate910 = MydateOrigin + YearEnd()

stocksdata2.index = stocksdata1.index + pd.tseries.offsets.MonthBegin()


