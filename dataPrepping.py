import pandas as pd
def getReturns(Path):
    data = pd.read_csv(Path, header= [0,1],index_col=0,parse_dates=True)
    returns = data["Close"] - data["Open"]
    return returns
    
 
jointReturns = getReturns("data/StockData.csv")
print(jointReturns)
