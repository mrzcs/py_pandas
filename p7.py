# Pickling
import pandas as pd
import quandl
import pickle

api_key = open('../quandlapikey.txt', 'r').read().rstrip('\n')


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

def readStateData():
    pickle_in = open('fiddy_states.pickle','rb')
    HPI_data = pickle.load(pickle_in)
    print(HPI_data)

grabInitialStateData()
readStateData()