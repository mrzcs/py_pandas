# building dataset
import pandas as pd
import quandl

api_key = open('../quandlapikey.txt', 'r').read()
""" print(api_key)
df = quandl.get("FMAC/HPI_TX", authtoken=api_key)

print(df.head()) """

fiddyStates = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#this is a list
#print(fiddyStates)
# this is the first dataframe
#print(fiddyStates[0])
#this is the second column
#print(fiddyStates[0][1])
#this is the second line
print(fiddyStates[0][1][1])

for abbr in fiddyStates[0][1][1:]:
    #print(abbr)
    print("FMAC/HPI_"+str(abbr))