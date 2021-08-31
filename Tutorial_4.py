# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:11:13 2021

@author: adelc
"""
###########Basic Filtering#####

import pandas as pd
people={
        "first":["corey","jane","john"],
        "last":["schafer","Doe", "Doe"],
        "email":["CoreyMSchafer@gmail.com","JaneDoe@email.com",
                 "JohnDoe@email.com"]}
df_from_people=pd.DataFrame(people)
###boolean condition
cond=(df_from_people["last"]=="Doe")
df_from_people[cond]
#using label
df_from_people.loc[cond]
#using loc and col
df_from_people.loc[cond,"email"]
########Multiple and boolean mask
john_doe_cond=(df_from_people["last"]=="Doe") &(df_from_people["first"]=="john")
df_from_people.loc[john_doe_cond]
#Multiple boolean mask or#
cond3=(df_from_people["last"]=="Doe") |(df_from_people["first"]=="john")
df_from_people.loc[cond3]
df_from_people.loc[~cond3]
##########Advanced Filtering on the survey dataset
data=pd.read_csv("Data/survey_results_public.csv",index_col="Respondent")
data_scheme=pd.read_csv("Data/survey_results_schema.csv",index_col="Column")
data_scheme
#####filter high salaries
high_salaries=data["ConvertedComp"]>70000
high_salaries_df=data.loc[high_salaries,["Country","LanguageWorkedWith","ConvertedComp"]]
####some countries only+high salary
countries=["United States","India","United Kingdom","Germany","Canada"]
cond=data["Country"].isin(countries)
data.loc[cond,"Country"]
###
filt=data["LanguageWorkedWith"].str.contains("Python",na=False)
data_python_only=data["LanguageWorkedWith"].loc[filt]
