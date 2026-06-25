import dataPrepping as DP
import pandas as pd

returns = DP.getReturns("data/StockData.csv")
print(returns)