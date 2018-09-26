import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

def createDF():
    web_stats = {'Day':[1,2,3,4,5,6],
            'Visitors':[43,34,65,56,29,76],
            'Bounce Rate':[65,67,78,65,45,52]}

    df = pd.DataFrame(web_stats)
    print('\noriginal DF: \n',df)
    return df

def indexDF(df):
    df = df.set_index('Day')
    #df.set_index('Day', inplace=True)
    print('\nafter set index: \n',df)
    return df

def printDF(df):
    print('\nhead: \n',df.head(3))
    print('\ntail: \n',df.tail(3))
    print('\nsingle col: \n',df.Visitors)
    print('\nsingle col: \n',df['Bounce Rate'])
    print('\nmultiple col: \n',df[['Visitors','Bounce Rate']])

def pltDF(df):
    df.Visitors.plot()
    plt.show()

def pltAllDF(df):
    df.plot()
    plt.show()


if __name__ == '__main__':
    df = createDF()
    df = indexDF(df)

    printDF(df)
    # pltDF(df)
    #pltAllDF(df)
    