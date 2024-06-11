import matplotlib.pyplot as plt
import pandas as pd

def createHistogram():
    cars = pd.read_csv('cars.csv')
    a = cars['disp']
    # Creating histrogram
    plt.hist(a, bins=[0,40,80,120,160,200,240,280])
    plt.show()


def customizeHistogram():
    cars = pd.read_csv('cars.csv')
    a = cars['disp']
    # Creating histrogram
    plt.hist(a, bins=[0,40,80,120,160,200,240,280,320,360,400], color = 'r', edgecolor='b')
    plt.title('Histrogram Demo')
    plt.xlabel('Range of Values')
    plt.ylabel('Frequesncy of value')
    plt.show()




customizeHistogram()
# createHistogram()
