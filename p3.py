# IO basics

import pandas as pd

# import csv file
df = pd.read_csv('ZILLOW-Z77006_ZRISFRR.csv')

# set index after import
df.set_index('Date', inplace=True)
#print(df.head())

# export file to csv
df.to_csv('newcsv2.csv')
#df.Value.to_csv('newcsv2.csv')

# set index when import
df = pd.read_csv('newcsv2.csv', index_col=0)

# change the column names
df.columns = ['House_Prices']

# export
df.to_csv('newcsv3.csv')

# export without header
df.to_csv('newcsv4.csv', header=False)

# import headless file,  giving the column names of Date and House_Prices
df = pd.read_csv('newcsv4.csv', names=['Date', 'House_Prices'], index_col=0)
print(df.head())

df.to_html('example.html')

# rename just one of the columns
df = pd.read_csv('newcsv4.csv', names = ['Date','House_Price'])
print(df.head())
df.rename(columns={'House_Price':'Prices'}, inplace=True)
print(df.head())