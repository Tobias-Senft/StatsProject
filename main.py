import dataPrepping as DP
import loadData as LD
import pandas as pd

Stocks = [
    "AAPL", # Appel
    "GOOGL", # Googel
    "MSFT", # Microsoft
    "NVO", # Novo Nordisk
    "NVDA", # Nvidia
    "AMD", # Advanced Micro Devices
    "CAT", # Caterpillar
    "LMT", # Lockhead Martin Corporation
    "^GSPC" # S&P 500
        ]
# Uncomment when if we would like to change the data in SockData.csv
# LD.UpdateLocalData(Stocks,"1y","data/StockData.csv")

dataPath = "data/StockData.csv"
returns = DP.getReturns(dataPath)
print(f"Description of data \n {returns.describe()}")
print(f"Anual Middel value \n {returns.mean()*252}")
print(f"returns: \n {returns.corr()}")

