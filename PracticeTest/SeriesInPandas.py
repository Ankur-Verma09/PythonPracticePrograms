import pandas as pd

def seriesObj():
    data = [1,2,3,4]
    series1 = pd.Series(data)
    print(series1)

def seriesObjType():
    data = [1,2,3,4]
    series1 = pd.Series(data)
    print(series1)
    print(type(series1))

def changeIndexOfASeriesObj():
    data = [1,2,3,4]
    series1 = pd.Series(data, index=['a','b','c','d'])
    print(series1)


# seriesObjType()
changeIndexOfASeriesObj()