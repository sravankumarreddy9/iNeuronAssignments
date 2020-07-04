# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:59:30 2020

@author: reddymv
"""
import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

#1. filling missing values
df.isna
df['FlightNumber']
for i in np.arange(1, df.From_To.count()+1):
    if pd.isnull(df.FlightNumber.loc[i,]):
        df.loc[i, 'FlightNumber'] = df.FlightNumber.loc[i-1,]+10

df['FlightNumber'].astype(int)

#2 split
temp_df = df.copy()
temp_df[['From','To']] = temp_df.From_To.str.split("_", expand=True)
temp_df


#3 formatting strings
temp_df.From_To = temp_df.From_To.str.capitalize()
temp_df.From = temp_df.From.str.capitalize()
temp_df.To = temp_df.To.str.capitalize()

#4 replacing col
df = df.drop('From_To', axis=1)
df['From_To'] = temp_df['From_To']

#5 delays
df1 = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
    
rows = []
_ = df1.apply(lambda row:[rows.append([row['Airline'], row['FlightNumber'], nn, row['From_To']]) 
        for nn in row.RecentDelays], axis=1)
rows
df_2 = pd.DataFrame(rows, columns = df.columns)
df_3 = pd.DataFrame(df['RecentDelays'].values.tolist())
len_cols = df_3.shape[1]
col_list = []
col_dict = {}
for i in range(len_cols):
    key = df_3.columns[i]
    value = "Delay" + str(i+1)
    col_dict[key] = value
df_3.rename(columns = col_dict, inplace =True)
df[["Delay1","Delay2","Delay3"]] = df_3[["Delay1", "Delay2", "Delay3"]]
df= df.drop('RecentDelays', axis=1)
df['Delay1'] = df['Delay1'].fillna(method='ffill', axis=0)
df['Delay2'] = df['Delay2'].fillna(method='ffill', axis=0)
df['Delay3'] = df['Delay3'].fillna(method='ffill', axis=0)
