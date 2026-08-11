from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf


#load stock
def load(name, time):
    return yf.download(name, period=time)

#Add functionality to compare two different stocks


if __name__ == '__main__':
    stock = input('Input the Ticker you would like to visualize: ').upper()
    timeperiod = input(f'What length of time would you like to visualize?\n'
                       f'(Format: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max):  ')
    df = load(stock, timeperiod)
    dfdates = df.index
    dfopen = df['Open']
    dfclose = df['Close']
    dfhigh = df['High']
    dflow = df['Low']
    dfvol = df['Volume']
    mavg = dfclose.rolling(20).mean()
    full_graph_mavg = dfclose.rolling(20, min_periods=1).mean()

    figure, axes = plt.subplots(3,2)
    #figure.delaxes(axes[2, 1])
    #print(dfdates)

    #plt.plot(range(dfdates.size), dfclose)
    axes[0, 0].plot(dfdates, dfopen)
    axes[0, 1].plot(dfdates, dfclose)
    axes[1, 0].plot(dfdates, dfhigh)
    axes[1, 1].plot(dfdates, dflow)
    axes[2, 0].plot(dfdates, dfvol)
    axes[2, 1].plot(dfdates, mavg)
    #axes.ylabel('Points')
    #axes.xlabel('Date of Close')
    #plt.title(f"{stock} Closing Prices")
    plt.tight_layout()
    plt.show()
    print(f'Number of Trading Days: {dfdates.size}\n'
          f'Starting Date: {dfdates[0].date()}\n'
          f'End Date: {dfdates[-1].date()}\n\n'
          'Closing Data: \n'
          #f'{dfclose["AAPL"]}'
          #f'{df.columns}'
          #f'{df.columns.nlevels}'
          #each of these functions returns a series under the column "stock"
          f'Highest Closing Price: {dfclose.max().iloc[0]:.1f} points\n'
          f'Lowest Closing Price: {dfclose.min().loc[stock]:.1f} points\n'
          f'Average Closing Price: {dfclose.mean()[stock]:.1f} points\n\n'
          'Gain & Loss Data: \n'
          f'Largest Day Gain: {(dfclose-dfopen).max()[stock]:.1f} points\n'
          f'Largest Day Loss: {(dfclose-dfopen).min()[stock]*(-1):.1f} points\n\n'
          #f'20 Day Rolling Average: {mavg}\n'
          #f'{dfclose.head(25)}'
          #f'{mavg.head(25)}'
          )