import pandas as pd
import numpy as np
def getReturns(Path):
    data = pd.read_csv(Path, header= [0,1],index_col=0,parse_dates=True)
    returns = data["Close"] - data["Open"]
    return returns
def getLogReturns(Path):
    data = pd.read_csv(Path, header= [0,1],index_col=0,parse_dates=True)
    returns = data["Close"] - data["Open"]
    return np.log(returns)