# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:02:49 2020

@author: kanwa
日期时间处理 datetime与Timestamp
"""

import pandas as pd
import datetime as dt
someday = dt.date(2020,3,19)
someday.day
someday.year
someday.month
sometime = dt.datetime(2020,3,19,8,13,57,897)
sometime.year
sometime.month
sometime.day
sometime.hour
sometime.minute
sometime.second
sometime.microsecond
# pandas Timestamp Object
pd.Timestamp('2020-03-19')
pd.Timestamp('2020/03/19')
pd.Timestamp('03/19/2020')
pd.Timestamp('13/12/2020')
pd.Timestamp('03/19/2020 08:34:32')
pd.Timestamp('03/19/2020 18:34:32')
pd.Timestamp(dt.date(2020,2,29))
Time1 = pd.Timestamp(dt.datetime(2020,2,29,21,34,32))
Time1.year
Time1.month
Time1.day
Time1.hour
Time1.minute
Time1.second
Time1.microsecond

 # pandas DateTimeIndex Object
dates = ["2020/03/01",'2020/03/04','2019/09/09']
pd.DatetimeIndex(dates)
type(pd.DatetimeIndex(dates))
dates = [dt.date(2020,3,4),dt.date(2020,3,14),dt.date(2020,3,24)]
dtIndex = pd.DatetimeIndex(dates)
values = [100,200,300]
dateindex = pd.Series(data = values,index = dtIndex)
# pandas to_datetime() Method
pd.to_datetime('2020-03-21')
pd.to_datetime(dt.date(2020,3,1))
pd.to_datetime(dt.datetime(2020,3,21,8,45,34))
pd.to_datetime(['2015-01-03','2020-03-2','2012','July, 4th,1996'])
times = pd.Series(['2015-01-03','2020-03-2','2012','July, 4th,1996'])
times
pd.to_datetime(times)
dates = pd.Series(['July 4th,1996','10/04/1990','hello','2014-0305'])
# errors{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’
# If ‘raise’, then invalid parsing will raise an exception.
# If ‘coerce’, then invalid parsing will be set as NaT.
# If ‘ignore’, then invalid parsing will return the input.
date1 = pd.to_datetime(dates,errors = 'coerce')
