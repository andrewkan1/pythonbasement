# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:41:41 2020
打开excel文件,获取多个sheet
@author: kanwa
"""

import pandas as pd

url = 'https://data.cityofnewyork.us/api/views/5cxm-c27f/files/bcdcc216-2de5-4ca0-bb40-cea412c14ed1?download=true&filename=2018%20-2019%20Arts%20Data%20Report.xlsx'
onlineexcel = pd.read_excel(url)
# csv文件只有一个sheet
employeesInfo = pd.read_csv(r'.\data\employeesinfo1.csv')
#  excel文件缺省打开第一个sheet
studentsInfo0 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx')
# excel文件可以有多个sheet
studentsInfo1 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = 'Sheet1')
studentsInfo2 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = 0)
studentsInfo3 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = 1)
# open多个sheet
studentsInfo4 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = ['ScoresOfStudents2018Spring','Sheet1'])
studentsInfo4Sheet1 = studentsInfo4['Sheet1']
studentsInfo4Sheet2 = studentsInfo4['ScoresOfStudents2018Spring']
# sheet_name = None时，open所有的sheet，该文件有5个sheet
studentsInfo5 = pd.read_excel(r'.\data\ScoresofStudents1.xlsx',sheet_name = None)
len(studentsInfo5 )
studentsInfo5sheet1 = studentsInfo5['Sheet1']
# ordereddict没有index
# studentsInfo5sheet2 = studentsInfo5[studentsInfo5.keys()[0]]
# 转变成list
studentsInfo5.keys()
values = studentsInfo5.values()
list(studentsInfo5.keys())
list(studentsInfo5.keys())[1]
list(studentsInfo5.keys())[0]

studentsInfo5sheet2 = studentsInfo5[list(studentsInfo5.keys())[1]]
studentsInfo5sheet3 = studentsInfo5[list(studentsInfo5.keys())[2]]
studentsInfo5sheet4 = studentsInfo5[list(studentsInfo5.keys())[3]]
studentsInfo5sheet5 = studentsInfo5[list(studentsInfo5.keys())[4]]



