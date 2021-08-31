# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:36:14 2021

@author: adelc
"""

#%%Tutorial 1##########
import pandas as pd
#import the csv data file
filename="data/survey_results_public.csv"
df=pd.read_csv(filename)
#get the shape of the dataset rows and cols
rows,cols=df.shape
print(f"the dataset has {rows} observations and {cols} variables")
#get more info (type of each variable +shape)
df.info()
#get a small sample of the data
df_sample=df.head(5)#first five obs
df_last=df.tail()
