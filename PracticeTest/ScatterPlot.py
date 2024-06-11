import matplotlib.pyplot as plt
import pandas as pd

def createScatterPlot():
    cars = pd.read_csv('cars.csv')
    a = cars['hp']
    b = cars['wt']
    x = range(32)
    plt.scatter(a,b)
    plt.scatter(a,x)
    plt.show()

def customizeScatterPlot():
    cars = pd.read_csv('cars.csv')
    a = cars['hp']
    b = cars['wt']
    x = range(32)
    plt.scatter(a,b, color = 'g', s = 300, edgecolors='y', marker='o', alpha=0.5)
    plt.scatter(a,x, color = 'r', s = 400, edgecolors='b', marker='2', alpha=1)
    plt.legend(['b','x'], loc='best', )
    plt.title('Scatter Plot Demo')
    plt.xlabel("X-Axis")
    plt.ylabel("X-Axis")
    plt.grid(True)
    plt.savefig('scatterPlot.png')
    plt.show()


customizeScatterPlot()
# createScatterPlot()