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

def calcVariance(DataPoints):
    sum = 0
    length = len(DataPoints)
    mean = np.mean(DataPoints)
    for Point in DataPoints:
        sum = sum + (Point - mean)**2
    return sum / (length - 1)

def covariance(x_Points,y_Points):
    sum = 0
    x_mean = np.mean(x_Points)
    y_mean = np.mean(y_Points)
    length = len(x_Points)
    for i in range(len(x_Points)):
        sum = (x_Points[i]-x_mean) * (y_Points[i]-y_mean)
    return sum / (length - 1)

def corelation(x_Points,y_Points):
    cov = covariance(x_Points,y_Points)
    x_std = np.sqrt(calcVariance(x_Points))
    y_std = np.sqrt(calcVariance(y_Points))
    return cov / (x_std * y_std)


print(corelation([1,3,4,5,6,1], 
                       [1,3,4,5,6,1]))
print(np.corrcoef([[1,5,4,4,6,1], [1,3,4,5,6,1]]))

