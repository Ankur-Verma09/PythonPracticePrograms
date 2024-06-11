import matplotlib.pyplot as plt
import pandas as pd

def createAreaChart():
    x = range(0,17)
    y = [1,5.6,9,6,1,5,2,8,5,1,7,2,2,1,5,6,8]

    # create Area plot
    plt.stackplot(x,y)
    plt.show()

def mergeAreaChartWithlineChart():
    cars = pd.read_csv('cars.csv')
    x = range(0,32)
    y = cars['hp']

    # create Area plot
    plt.stackplot(x,y, colors='black', alpha=0.5)
    plt.plot(x,y,color = 'r')
    plt.grid(True)
    plt.show()

# createAreaChart()
mergeAreaChartWithlineChart()

