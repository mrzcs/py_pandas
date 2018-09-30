# Percent Change and Correlation Tables
import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

quandl_api_key = open('../quandlapikey.txt', 'r').read().rstrip('\n')
#print(quandl_api_key)
quandl.ApiConfig.api_key = quandl_api_key


def stateList():
    fiddyStates = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddyStates[0][1][1:]

def grabInitialStateData():
    main_df =pd.DataFrame()
    states = stateList()

    for abbr in states:
        #print(abbr)
        query = 'FMAC/HPI_' + str(abbr)

        df = quandl.get(query)
        print(query)
        df.columns = [str(abbr)]
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open(file_name1, 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def grabInitialStateData2():
    main_df =pd.DataFrame()
    states = stateList()
    #states = ['AL']

    for abbr in states:
        #print(abbr)
        query = 'FMAC/HPI_' + str(abbr)

        df = quandl.get(query)
        print(query)
        df.columns = [str(abbr)]
        df = df.pct_change()
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    #print(main_df.head())

    pickle_out = open(file_name2, 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def grabInitialStateData3():
    main_df =pd.DataFrame()
    states = stateList()
    #states = ['AL']

    for abbr in states:
        #print(abbr)
        query = 'FMAC/HPI_' + str(abbr)

        df = quandl.get(query)
        print(query)
        df.columns = [str(abbr)]
        df[abbr] = (df[abbr]-df[abbr][0]) / df[abbr][0] * 100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    #print(main_df.head())

    pickle_out = open(file_name3, 'wb')
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

def HPIBenchmark():
    df = quandl.get('FMAC/HPI_USA')
    df.columns = [str('United States')]
    df['United States'] = (df['United States'] - df['United States'][0]) / df['United States'][0] * 100.0
    return df

file_name1 = 'fiddy_states.pickle'
file_name2 = 'fiddy_states2.pickle'
file_name3 = 'fiddy_states3.pickle'

#grabInitialStateData()
# change column value
#HPI_data['TX2'] = HPI_data['TX'] * 2
#print(HPI_data[['TX', 'TX2']].head())

#grabInitialStateData2()

#grabInitialStateData3()
""" calcPct(HPI_data)

HPI_data = readStateData(file_name2)
modifyStateData(HPI_data)
HPI_data = readStateData(file_name3)
print(HPI_data.head(5)) """


HPI_data = readStateData(file_name3)
#print(HPI_data.head(5))

benchmark = HPIBenchmark()
#print(benchmark.head(5))

#plotting
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data.plot(ax=ax1)
benchmark.plot(color='k', ax=ax1, linewidth=10)

plt.legend().remove()
plt.show()
