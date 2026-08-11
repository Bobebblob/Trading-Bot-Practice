from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf


#load stock
def load(name, time):
    return yf.download(name, period=time)

#display summary
#plot price
#plot volume
#calculate returns
#find biggest gain
#find biggest loss
#plot moving average

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

    figure, axes = plt.subplots(3,2)
    figure.delaxes(axes[2, 1])

    #print(dfdates)

    #plt.plot(range(dfdates.size), dfclose)
    axes[0, 0].plot(dfdates, dfopen)
    axes[0, 1].plot(dfdates, dfclose)
    axes[1, 0].plot(dfdates, dfhigh)
    axes[1, 1].plot(dfdates, dflow)
    axes[2, 0].plot(dfdates, dfvol)
    #axes.ylabel('Points')
    #axes.xlabel('Date of Close')
    #plt.title(f"{stock} Closing Prices")
    plt.tight_layout()
    plt.show()
    print(f'Number of Trading Days: {dfdates.size}\n'
          f'Starting Date: {dfdates[0].tz_localize(None)}\n'
          f'End Date: {dfdates[-1].tz_localize(None)}\n')