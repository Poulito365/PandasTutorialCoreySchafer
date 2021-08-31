# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:55:50 2021

@author: adelc
"""
#%%Load everything from Tutorial_1
import Tutorial_1
import pandas as pd
#%%Pandas Dataframe and Dictionnary
people={
        "first":["corey","jane","john"],
        "second":["schafer","Doe", "Doe"],
        "email":["CoreyMSchafer@gmail.com","JaneDoe@email.com",
                 "JohnDoe@email.com"]}
df_from_people=pd.DataFrame(people)
#%%access column of a df
#access the column first
First=df_from_people["first"]
type(First)#this is a series
type(df_from_people[["first"]])#this is a dataframe
#access column first and last
sub_df=df_from_people[["first","email"]]
#get a list of all df columns
df_from_people.columns
#%%Accessing elements via index location (iloc)
df_from_people.iloc[[0,2],2]
#access element via label
df.loc[0,"Hobbyist"]
