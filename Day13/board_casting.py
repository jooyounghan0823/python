import yfinance

netflix = yfinance.Ticker('AAFL')
netflix_info = netflix.info
print(netflix_info['regularMarketPrice'])


