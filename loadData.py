import yfinance as yf
import pandas as pd


# pulling data from API putting it into csv for easier use
data = pd.DataFrame(yf.download(["AAPL", "MSFT", "GOOGL"],period="1y"))
data.to_csv("data/StockData.csv",index=False)