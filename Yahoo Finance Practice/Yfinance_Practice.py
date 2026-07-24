import yfinance as yf
import pandas as pd

apple_ticker = yf.Ticker('AAPL') #Apple Stock Ticker

#print(apple_ticker.info["open"])
#print(apple_ticker.analyst_price_targets)
#print(apple_ticker.quarterly_balance_sheet.to_string())
#print(apple_ticker.news)
#print(apple_ticker.calendar)

df = apple_ticker.history(period='max')
open_price = df["Open"]

#print(apple_ticker.history(period='6d').to_string())
#print(apple_ticker.history(period='1mo').to_string())
#print(apple_ticker.history(period='1y'))
#print(apple_ticker.history(period='ytd'))
#print(df)
#print(open_price)
#print(apple_ticker.options)
#print(apple_ticker.option_chain(apple_ticker.options[0]))
#print(apple_ticker.option_chain(apple_ticker.options[0]).calls)
#print(apple_ticker.option_chain(apple_ticker.options[0]).puts)

spy = yf.Ticker('SPY')
Nasdaq100 = yf.Ticker('QQQ')

#print(spy.funds_data.sector_weightings)
#print(Nasdaq100.funds_data.sector_weightings)
#print(Nasdaq100.funds_data.top_holdings)
#print(Nasdaq100.funds_data.description)

market = yf.Tickers(['AAPL', 'GOOG', 'MSFT'])
microsoft = market.tickers['MSFT']

#print(market.history())
#print(microsoft.history())

stock_data = yf.download(["AAPL", "MSFT"])

