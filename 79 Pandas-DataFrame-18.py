# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:39:33 2020
日期时间处理 date_range
@author: kanwa

"""

import pandas as pd


# 在固定的时间段内，依照频率，创建时间索引数据，Create range of dates with the pd.date_range() method 
times1 = pd.date_range(start ='1998-01-01',end = '2020-03-01',freq = 'Y')
times2 = pd.date_range(start ='1998-12-21',end = '1999-01-11',freq = 'D')
type(times2)
type(times2[0])
times3 = pd.date_range(start ='2000-01-01',end = '2020-03-03',freq = '3D')
# B represents Business day
times4 = pd.date_range(start ='2000-01-01',end = '2020-01-11',freq = 'B')
# W weekly frequency
times5 = pd.date_range(start ='2000-02-02',end = '2020-02-19',freq = 'W')
# W-FRI weekly frequency (Fridays)
times6 = pd.date_range(start ='2000-03-03',end = '2020-03-19',freq = 'W-FRI')
# H hourly frequency
times7 = pd.date_range(start ='2000/04/01',end = '2020-04-19',freq = '5H')
# M month end frequency  MS month start frequency
times8 = pd.date_range(start ='05/05/2001',end = '2020-04-19',freq = 'M')
times9 = pd.date_range(start ='2002/06/06',end = '2020-06-19',freq = 'MS')
# A, Y year end frequency  AS, YS year start frequency
times10 = pd.date_range(start ='1999-01-01',end = '2020-07-19',freq = 'A')
times11 = pd.date_range(start ='1999-01-01',end = '2020-07-19',freq = 'YS')
# 固定间隔次数 periods
timesperiods1 = pd.date_range(start ='2020-01-01',periods = 25, freq = 'D')
timesperiods2 = pd.date_range(start ='2020-01-01',periods = 50, freq = 'D')
timesperiods3 = pd.date_range(start ='2020-01-01',periods = 50, freq = 'B')
timesperiods4 = pd.date_range(start ='2020-01-01',periods = 50, freq = 'W')
timesperiods5 = pd.date_range(start ='2020-01-01',periods = 50, freq = 'W-SUN')
timesperiods6 = pd.date_range(start ='2020-01-01',periods = 50, freq = 'W-TUE')
timesperiods7 = pd.date_range(start ='2020-01-01',periods = 50, freq = 'MS')
timesperiods8 = pd.date_range(start ='2020-01-01',periods = 50, freq = 'H')
timesperiods9 = pd.date_range(start ='2020-01-01',periods = 50, freq = '6H')
# 固定间隔次数 periods
timesperiods10 = pd.date_range(end = '2020-06-30',periods = 20, freq = 'D')
timesperiods11 = pd.date_range(end = '2020-06-30',periods = 40, freq = 'B')
timesperiods12 = pd.date_range(end = '2020-06-30',periods = 40, freq = 'W-SUN')
timesperiods13 = pd.date_range(end = '2020-06-30',periods = 40, freq = 'W-FRI')
timesperiods14 = pd.date_range(end = '2020-06-30',periods = 40, freq = 'M')
timesperiods15 = pd.date_range(end = '2020-06-30',periods = 40, freq = 'MS')
timesperiods16 = pd.date_range(end = '2020-06-30',periods = 40, freq = '7H')
