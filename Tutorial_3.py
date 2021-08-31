# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:15:50 2021

@author: adelc
"""


######Python tutorial 3
#%%create the data frame
import pandas as pd
people={
        "first":["corey","jane","john"],
        "second":["schafer","Doe", "Doe"],
        "email":["CoreyMSchafer@gmail.com","JaneDoe@email.com",
                 "JohnDoe@email.com"]}
df_from_people=pd.DataFrame(people)
#set the email as the new index
df_from_people.set_index("email")
#modify inplace
df_from_people.set_index("email",inplace=True)  
#get the list of all indexes
df_from_people.index
#access information by label
df_from_people.loc['CoreyMSchafer@gmail.com',"second"]
#reset the index back
df_from_people.reset_index(inplace=True)
#########setting the index directly
data=pd.read_csv("Data/survey_results_public.csv",index_col="Respondent")
data.head()
schema_data=pd.read_csv("Data/survey_results_schema.csv")
schema_data.set_index("Column",inplace=True)
#access to respondent 1
data.loc[1]
#access the question for hobyist
schema_data.loc["Hobbyist","QuestionText"]
schema_data.sort_index()
schema_data.sort_index(ascending=False)
