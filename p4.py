# building dataset
import pandas as pd
import quandl

""" api_key = open('../quandlapikey.txt', 'r').read()
df = quandl.get("FMAC/HPI_TX", authtoken=api_key)

print(df.head()) """

fiddyStates = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddyStates)