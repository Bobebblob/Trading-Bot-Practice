import yfinance as yf
from yfinance import EquityQuery

objecta = EquityQuery(
    'and', [
        EquityQuery('eq', ['region', 'us']),
        EquityQuery('gt', ['percentchange', 3])
    ]
)

results = yf.screen(objecta, sortField='percentchange', sortAsc=False)
#print(results)

#for i in results['quotes']:
#    print(i['symbol'], i.get('displayName'), i.get('regularMarketChangePercent'))

websocket = yf.WebSocket()

websocket.subscribe(["NVDA"])
websocket.listen(print)

"""
yf.config.network.proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "https://127.0.0.1:8080"
}
yf.config.network.retries = 2
yf.config.debug.logging = True
yf.config.debug.hide_exceptions = False

df = yf.Ticker("AAPL").history(period='5d')
print(df.tail())
"""


"""
import asyncio

async def main():
    webs = yf.AsyncWebSocket(verbose=False)
    
    await webs.subscribe(["AAPL"])
    
    async def on_message(msg):
        print(msg)
        
    await webs.listen(on_message)
    
asyncio.run(main())
"""