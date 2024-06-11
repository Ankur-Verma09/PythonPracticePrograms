import pandas as pd

def importDataSet():
    cars = pd.read_csv("cars.csv")
    # print(cars)
    # print(type(cars))
    # print(cars.head()) # 1st five record
    # print(cars.head(10))  # 1st ten record
    # print(cars.tail())  # last five record
    # print(cars.tail(10))  # last ten record
    # print(cars.shape)  # return total number of rows and columns
    # print(cars.info())  # returns the consise summery of the column
    # print(cars.mean()) # returns mean of the dataset
    # print(cars.median())  # returns median of the dataset
    # print(cars.std())  # returns standard dev of the dataset
    # print(cars.max())  # returns max of the dataset
    # print(cars.min())  # returns min of the dataset
    # print(cars.count())  # returns count of the dataset
    print(cars.describe())  # returns describe statics of the dataset (Count, mean.std, min, 25%, 50%, 75%, max)



importDataSet()