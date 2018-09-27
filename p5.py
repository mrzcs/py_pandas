# concatenating and appending dataframes

import pandas as pd

def createDF():
    df1 = pd.DataFrame({'HPI':[80,85,88,85],
                        'Int_rate':[2,3,2,2],
                        'US_GDP_Thousands':[50,55,65,55]},
                        index = [2001,2002,2003,2004])

    df2 = pd.DataFrame({'HPI':[80,85,88,85],
                        'Int_rate':[2,3,2,2],
                        'US_GDP_Thousands':[50,55,65,55]},
                        index = [2005,2006,2007,2008])

    df3 = pd.DataFrame({'HPI':[80,85,88,85],
                        'Int_rate':[2,3,2,2],
                        'Low_tier_HPI':[50,52,50,53]},
                        index = [2001,2002,2003,2004])
    return df1, df2, df3

def contM1(df1, df2):
    concat = pd.concat([df1, df2])
    print(concat)

def contM2(df1, df2, df3):
    concat = pd.concat([df1, df2, df3])
    print(concat)

if __name__ == '__main__':
    df1, df2, df3 = createDF()
    #contM1(df1, df2)
    #contM2(df1, df2, df3)

    #appending
    df4 = df1.append(df3)
    #print(df4)

    #append series
    s = pd.Series([99,2,50], index=['HPI', 'Int_rate', 'US_GDP_Thousands'])
    df4 = df1.append(s, ignore_index=True)
    print(df4)

    s = pd.Series([99,2,50], index=['HPI', 'Int_rate', 'US_GDP_Thousands'], name='s1')
    df5 = df1.append(s, ignore_index=False)
    print(df5)