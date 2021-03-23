# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:00:10 2020
设置显示选项
@author: kanwa
"""

import pandas as pd
import numpy as np
# 改变显示选项
# 产生数组200*30 每个元素随机值0-100
data = np.random.randint(100,size=(200,30))
Mydf = pd.DataFrame(data)
Mydf.head(100)
Mydf.tail(200)
# 设置显示的最多行数，也可以改变其值
pd.options.display.max_rows
pd.options.display.max_rows = 6
# 设置显示的最多列数，也可以改变其值
pd.options.display.max_columns = 6
pd.options.display.max_columns
# 使用方法
pd.get_option('max_rows')
pd.get_option('max_columns')
pd.set_option('max_rows',5)
pd.set_option('max_columns',6)
pd.reset_option('max_rows')
pd.get_option('max_rows')
pd.reset_option('max_columns')
pd.get_option('max_columns')
# 显示精度设置
Mydf1 = pd.DataFrame(np.random.randn(3,3))
pd.get_option('precision')
pd.set_option('precision',2)
Mydf1
pd.reset_option('precision')
