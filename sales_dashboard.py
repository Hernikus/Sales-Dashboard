#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:09:23 2023

@author: hernikusuma
"""

import pandas as pd

# file_name = pd.read_csv ('file.csv') <--- format of read_csv

# data_sales = pd.read_csv('transaction.csv') <-- pay attention with separator
data_sales = pd.read_csv('transaction.csv', sep=';')

#define variables and mathematics operation


#CostPerTransaction
data_sales['CostPerTransaction'] = data_sales['CostPerItem'] * data_sales['NumberOfItemsPurchased']

#SalesPerTransaction
data_sales['SalesPerTransaction'] = data_sales['SellingPricePerItem'] * data_sales ['NumberOfItemsPurchased']

#ProfitPerTransaction
data_sales['ProfitPerTransaction'] = data_sales['SalesPerTransaction']-data_sales['CostPerTransaction']

#MarkUp
data_sales['MarkUpPrice'] = data_sales['ProfitPerTransaction']/data_sales['CostPerTransaction']

data_sales.info()

#Rounding MarkUp Column
data_sales['MarkUpPrice'] = round(data_sales['MarkUpPrice'],2)

#checking column data type
print(data_sales['Day'].dtype)

#Change column datatype
day = data_sales['Day'].astype(str)
year = data_sales['Year'].astype(str)

#Combine the column to make new column
date = day+'-'+data_sales['Month']+'-'+year
data_sales['Date'] = date

# Trying to see spesific data
data_sales.iloc[0] #show data index 0 or row 1 but all column

data_sales.iloc[0,2] #row 1 column 2 

data_sales.head(2) #2 row al data

data_sales.iloc[0:2,3]

# create split column 
# column_var = column.str.split(':', expand = True)

split_col = data_sales['ClientKeywords'].str.split(',', expand=True)

# divide split column to new column
data_sales['ClientAge'] = split_col[0]
data_sales['ClientType'] = split_col[1]
data_sales['ClientLengthOfContract'] = split_col[2]

# replace function
data_sales['ClientAge'] = data_sales['ClientAge'].str.replace('[','') 
data_sales['ClientLengthOfContract'] = data_sales['ClientLengthOfContract'].str.replace(']','')
data_sales['Date'] = data_sales['Date'].str.replace('2018','2020')
data_sales['Date'] = data_sales['Date'].str.replace('2019','2021')
data_sales['Date'] = data_sales['Date'].str.replace('2028','2022')
# change letter function
data_sales['ItemDescription'] = data_sales['ItemDescription'].str.capitalize()

# bringing in a new dataset
data_season = pd.read_csv('value_inc_seasons.csv', sep=';')

# merge data
data_sales = pd.merge(data_sales, data_season, on='Month')

# drop some data
data_sales = data_sales.drop('Day', axis=1)
data_sales = data_sales.drop('Month', axis=1)
data_sales = data_sales.drop('Year', axis=1)
data_sales = data_sales.drop('ClientKeywords', axis=1)

# make a new csv for cleaned data
# data_sales.to_csv('ValueInc_Cleaned.csv', index=False)

#get summaries of the data

data_sales.info()













