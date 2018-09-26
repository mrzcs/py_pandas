# basic IO of pandas

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

# import source not having header
df = pd.read_csv('newcsv4.csv', names=['Date', 'House_Prices'], index_col=0)
print(df.head())

df.to_html('example.html')

df.rename('newcsv4.csv', name)