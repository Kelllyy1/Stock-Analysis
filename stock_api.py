import yfinance as yf

# Define the ticker symbol for the stock I'm interested in
ticker_symbol = 'VOO'

# Fetch data for this ticker
ticker_data = yf.Ticker(ticker_symbol)

# Fetch the latest closing price
#  .info provides a dictionary with various information about the stock
# We're specifically interested in the 'previous close' price
latest_price = ticker_data.info['previousClose']

print(f"The latest closing price of {ticker_symbol} is: ${latest_price}")
print("Done")