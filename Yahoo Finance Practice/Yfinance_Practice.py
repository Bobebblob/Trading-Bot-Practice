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

stock_data = yf.download(["AAPL", "MSFT"]) #just prices

us_market = yf.Market('US')

#print(us_market.status)
#print(us_market.summary) #also shows indices of that market

tech_sector = yf.Sector("technology")

#print(tech_sector.industries)
#print(tech_sector.top_companies)

this_month = yf.Calendars(start='2026-04-01', end='2026-05-01')

#print(this_month.earnings_calendar.to_string())
#print(this_month.economic_events_calendar)
#print(this_month.ipo_info_calendar)
#print(this_month.splits_calendar)

#print(this_month.calendars)

#apple_search = yf.Lookup('apple')

#print(apple_search.stock)

actual_apple = yf.Search('apple', max_results=5, news_count=3)

#print(actual_apple.quotes)
print(actual_apple.news)