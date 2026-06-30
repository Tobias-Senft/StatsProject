import yfinance as yf
import pandas as pd


# pulling data from API putting it into csv for easier use
# Stock = ["AAPL","GOOGL","MSFT"]
# "1y"
# DataPath = "data/StockData.csv"
def UpdateLocalData(Stock,Time,DataPath):
    data = pd.DataFrame(yf.download(Stock,period=Time))
    data.to_csv(DataPath)