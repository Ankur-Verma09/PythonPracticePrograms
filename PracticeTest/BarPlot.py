import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def verticalBarPlotOnCars():
    cars = pd.read_csv('cars.csv')
    y = cars['hp']
    x = range(32)
    x1 = cars['model'].tolist()
    fig = plt.figure(figsize=(16,8))
    plt.bar(x1,y, color = 'blue', alpha = 0.5)
    plt.show()

def horizontalBarPlotOnCars():
    cars = pd.read_csv('cars.csv')
    y = cars['hp']
    x = range(32)
    x1 = cars['model'].tolist()
    fig = plt.figure(figsize=(16,8))
    plt.barh(x1,y, color = 'blue', alpha = 0.5)
    plt.show()

horizontalBarPlotOnCars()
