import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def areaLinePlot():
    cars = pd.read_csv('cars.csv')
    y1 = cars['hp']
    y2 = cars['disp']
    x = range(32)
    plt.plot(x,y1, color = 'red')
    plt.stackplot(x,y1, colors = 'yellow', alpha=0.7)
    plt.plot(x, y2, color='black')
    plt.stackplot(x, y2, colors='blue', alpha=0.5)
    plt.show()


areaLinePlot()