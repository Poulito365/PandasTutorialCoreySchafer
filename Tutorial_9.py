# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:37:54 2021

@author: adelc
"""

import pandas as pd
import numpy as np
from pathlib import Path
people={"first":["Corey","Jane","John","Chris",np.nan,None,"NA"],
        "last":["Schafer","Doe","Doe","Schafer",np.nan,np.nan,"Missing"],
        "email":["CoreyMschafer@gmail.com","JaneDoe@email.com","JohnDoe@email.com",None,"Anonymous@email.com",np.nan,np.nan],
        "age":["33","55","63","36",None,None,"Missing"]}
df=pd.DataFrame(people)
#####################1.Dropping NAN############
df_dropped_any_index=df.dropna()
df_dropped_na_all_index=df.dropna(axis="index",how="all")
df_dropped_columns_an_col=df.dropna(axis="columns",how="any")
df_subset=df.dropna(axis="index",how="any",subset=["email"])
df_own_rep=df.replace(("NA","Missing"),np.nan)
##############2.detecting NAN##########"
df.isna()
df.fillna("MISSING")
df.fillna(0)
df.dtypes
df["age"].mean()
########casting data type
#nan are floats
type(np.nan)
df.replace(["NA","Missing"],np.nan,inplace=True)
df["age"]=df["age"].astype(float)
df.dtypes
df["age"].mean()
#######Real data set#########
df=pd.read_csv("Data/survey_results_public.csv")
df["YearsCode"].head()
df["YearsCode"].mean()
df["YearsCode"].astype(float).mean()
df["YearsCode"].unique()
####replace unique values##
df["YearsCode"].replace({"Less than 1 year": 0,"More than 50 years":50}).astype(float).mean()
