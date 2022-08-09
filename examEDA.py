# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 14:29:15 2022

@author: Kgopotso
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


# BRINGING IN THE DATA
data = pd.read_csv('exams_prac.csv') 

# CLEANING THE DATA 
print(data.columns.tolist()) 
split_col = data['gender,"race/ethnicity","parental level of education","lunch","test preparation course","math score","reading score","writing score"'].str.split(',', expand=True) 

data['Gender'] = split_col[0]
data['race'] = split_col[1]
data['parent education'] = split_col[2]
data['lunch'] = split_col[3] 
data['test prep'] = split_col[4]
data['math score'] = split_col[5] 
data['reading score'] = split_col[6]
data['writing score'] = split_col[7] 

data = data.drop('gender,"race/ethnicity","parental level of education","lunch","test preparation course","math score","reading score","writing score"', axis=1) 

data = data.drop('race', axis=1) 
data = data.drop('parent education', axis=1) 

data.describe() 
data.info()  

    # checking data type
print(data['math score'].dtype) 


# RELATIONSHIP ANALYSIS 
lunchplot = data.groupby(['lunch']).size()
lunchplot.plot.bar(color = 'green', width = 0.1) 
plt.show() 

testprepplot= data.groupby(['test prep']).size() 
testprepplot.plot.bar(color= 'red', width = 0.1)
plt.show()  

mathplot = data.groupby(['math score']).size() 
mathplot.plot.bar(color='black', width = 0.2)
plt.show() 


  #  scatter plots 
x = data['writing score']
y = data['reading score']
plt.scatter(x, y, color= '#4caf50') 
plt.show() 

# writing it back to excel 
data.to_excel('exam_prac_cleaned.xlsx', sheet_name='examdata', index=False) 