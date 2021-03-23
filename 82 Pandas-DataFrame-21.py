# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:04:03 2020
用日期过滤数据 截断数据 时间差
@author: kanwa
"""
import pandas as pd
import datetime as dt
from pandas_datareader import data

# 用日期过滤数据
eventdays = pd.date_range(start='2008-01-4',end = '2009-01-01',freq = pd.DateOffset(months=1))
stocksdata1 = data.DataReader(name = 'GOOG',data_source = 'yahoo',start = dt.date(2007,12,1), end = dt.datetime.now())
cond = stocksdata1.index.isin(eventdays )
stocksdatacond = stocksdata1.loc[cond]

# 在第一字段前面插入一列代表星期几 名字是Day of Week 值是stocks.index.weekday_name
stocksdata1.insert(0,'Day of Week', stocksdata1.index.weekday_name)
stocksdata1.insert(1,"Is Start of Month",stocksdata1.index.is_month_start)
stocksdata2 = stocksdata1[stocksdata1['Is Start of Month']]


# 截断数据.truncate() Method
company ="GOOG"
start = '2008-01-4'
end = '2019-01-01'
stocks = data.DataReader(name = company,data_source = 'yahoo',start = start, end = end)
stockstruncate1 = stocks.truncate(before ='2013-02-05',after ='2013-03-03'  )
stockstruncate2 = stocks.truncate(before ='2013-02-09',after ='2013-03-28'  )

# 时间差 pandas timedelta objects
timea = pd.Timestamp('2016-02-01 04:35:15')
timeb = pd.Timestamp('2016-03-20 23:23:13')
timeb - timea
type(timeb - timea)
pd.Timedelta(days = 3,minutes = 45,hours = 12, weeks = 8)
timec = pd.Timedelta('14 days 6 hours 12 minutes 49 seconds')
type(timec)
timesum = timea + timec

# 时间差 Timedeltas in a dataset
employeesInfo0 = pd.read_csv(r'.\data\employeesinfo1.csv')
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv', parse_dates =['Date of Birth','Date of Joining Firm','Last Login Time'] )
employeesInfo.dtypes
employeesInfo["Ages"] = dt.datetime.now() - employeesInfo["Date of Birth"]
employeesInfo['Years of Ages'] = dt.datetime.now().year - employeesInfo["Date of Birth"].dt.year
employeesInfo['Sevice of years'] = dt.datetime(2020,6,3) - employeesInfo["Date of Joining Firm"]
employeesInfo['Sevice of years1'] = dt.datetime(2020,6,3).year - employeesInfo["Date of Joining Firm"].dt.year
cond = employeesInfo['Sevice of years'] > '3650 days'
employeesInfo1 = employeesInfo[cond]

# 举例
import numpy as np
timed = pd.Timedelta('30 minutes 01 seconds')
employeesInfo['New Last Login Time'] = (timed + employeesInfo['Last Login Time'])
employeesInfo['New Last Login Time'] = np.where(employeesInfo['Team']=='Marketing', 
                                                timed + employeesInfo['Last Login Time'], employeesInfo['Last Login Time'])

