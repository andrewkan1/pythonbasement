# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:40:44 2020
pie饼图
@author: andrew
"""


import pandas as pd
import matplotlib.pyplot as plt

data = [20,30,70,60]
labels = ['C++','Java','Python','SQL']
# fig = plt.figure(figsize =(7,7)) 
# # Creating axes instance add_axes新增子区域 left, bottom, width, height = 0, 0, 1,1 
# ax = fig.add_axes([0,0,1,1]) 
# # ax.pie(data,labels=labels)
# # ax.pie(data,labels=labels,wedgeprops={'edgecolor':'yellow'})
# colors = ['red','green','pink','lightblue']
# # ax.pie(data,labels=labels,wedgeprops={'edgecolor':'yellow'},colors=colors)
# explode=(0,0,0.1,0)
# ax.pie(data,labels=labels,wedgeprops={'edgecolor':'yellow'},colors=colors,explode=explode)

# ax.pie(data,labels=labels,wedgeprops={'edgecolor':'yellow'},
#        colors=colors,explode=explode,shadow=True)

# ax.pie(data,labels=labels,wedgeprops={'edgecolor':'yellow'},
#        colors=colors,explode=explode,shadow=True,autopct='%1.1f%%')
# ax.pie(data,labels=labels,wedgeprops={'edgecolor':'yellow'},colors=colors,
#         explode=explode,shadow=True,autopct='%1.1f%%',startangle=90)
# plt.show()




rankofCode = pd.read_excel(r'.\data\rankofcodeLangusge.xlsx',sheet_name='codeLanguage')
labels = rankofCode['Programming Language']
ranks = rankofCode['Ratings']
ranks = ranks[:9]
other = pd.Series(1-sum(ranks[:9]))
ranks = ranks.append(other)
labels = list(labels[:9])
labels.append('other')
fig = plt.figure(figsize =(5,5)) 
# Creating axes instance add_axes新增子区域 left, bottom, width, height = 0, 0, 1,1 
ax = fig.add_axes([0,0,1,1]) 
explode=(0,0,0.1,0,0,0,0,0,0,0)
patches, texts,autotexts = ax.pie(ranks,labels=labels,wedgeprops={'edgecolor':'yellow'}, 
                                  explode=explode,shadow=True,autopct='%1.1f%%',startangle=90)
ax.legend(patches, labels,
          title="Ratings of Prgramming Languages",
          loc="best")
# plt.title('Ratings of Prgramming Languages')
plt.show()