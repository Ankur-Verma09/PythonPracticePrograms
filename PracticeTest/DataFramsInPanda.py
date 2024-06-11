import pandas as pd
import numpy as np

# Creating a DataFram using a list
def createDataFrame():
    data = [1,2,3,4,5]
    df = pd.DataFrame(data)
    print(df)


# Creating a DataFram using a Dictionary
def createDataFrameDic():
    dictionary = {'fruits': ['apple', 'banana', 'mangoes'],'count': [10,20,15]}
    df = pd.DataFrame(dictionary)
    print(df)

# Creating a DataFram using a Series
def createDataFrameSer():
    series = pd.Series([6,12], index=['a','b'])
    df = pd.DataFrame(series)
    print(df)

# Creating a DataFram using a Numpy Array
def createDataFrameNumpyArr():
    nparr = np.array([[50000,60000],['John', 'James']])
    df = pd.DataFrame({'name': nparr[1],'salary': nparr[0]})
    print(df)


# createDataFrame()
# createDataFrameDic()
# createDataFrameSer()
createDataFrameNumpyArr()