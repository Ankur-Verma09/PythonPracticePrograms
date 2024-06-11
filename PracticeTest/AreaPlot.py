import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def areaPlotOnCars():
    cars = pd.read_csv('cars.csv')
    y1 = cars['hp']
    y2 = cars['disp']
    x = range(32)
    plt.stackplot(x,y1, colors='red', alpha = 0.7)
    plt.stackplot(x, y2, colors='blue', alpha=0.5)
    plt.show()


areaPlotOnCars()