# Percent Change and Correlation Tables
import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('../quandlapikey.txt', 'r').read()

def stateList():
    fiddyStates = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddyStates[0][1][1:]

def grabInitialStateData():
    main_df =pd.DataFrame()
    states = stateList()

    for abbr in states:
        #print(abbr)
        query = 'FMAC/HPI_' + str(abbr)

        df = quandl.get(query,authtoken=api_key)
        print(query)
        df.columns = [str(abbr)]
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def readStateData(file_name):
    #pickle_in = open('fiddy_states.pickle','rb')
    #HPI_data = pickle.load(pickle_in)
    HPI_data = pd.read_pickle(file_name)
    return HPI_data

def calcPct(HPI_data):
    HPI_data_pct = HPI_data.pct_change()
    pickle_out = open('fiddy_states2.pickle','wb')
    pickle.dump(HPI_data_pct, pickle_out)
    pickle_out.close()

def modifyStateData(HPI_data):
    states = list(HPI_data.columns.values)
    #main_df = pd.DataFrame()
    print(states)
    for abbv in states:
        HPI_data[abbv] = (HPI_data[abbv]-HPI_data[abbv][0]) / HPI_data[abbv][0] * 100.0
            
    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(HPI_data, pickle_out)
    pickle_out.close()

file_name1 = 'fiddy_states.pickle'
file_name2 = 'fiddy_states2.pickle'
file_name3 = 'fiddy_states3.pickle'

HPI_data = readStateData(file_name1)
print(HPI_data.head(1))

#print(HPI_data.head())
#HPI_data['TX2'] = HPI_data['TX'] * 2
#print(HPI_data[['TX', 'TX2']].head())
calcPct(HPI_data)

HPI_data = readStateData(file_name2)
modifyStateData(HPI_data)
HPI_data = readStateData(file_name3) 
print(HPI_data.head(5))

#plotting
""" 
HPI_data.plot()
plt.legend().remove()
plt.show()
 """