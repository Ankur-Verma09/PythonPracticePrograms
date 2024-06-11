import matplotlib.pyplot as plt
import pandas as pd

def createViolinplot():
    a = [20,4,1,30,20,10,20,70,30,10]
    b = [10,3,1,15,17,2,30,44,2,1]
    c = [30,10,20,5,10,20,50,60,20,45]
    data = list([a,b,c])

    # ploting the box
    plt.violinplot(data, showmeans=True, showextrema=True)
    plt.title("Box plot Demo")
    plt.grid(True)
    plt.show()


def createViolinPlotOnCar():
    cars = pd.read_csv('cars.csv')
    a = cars['hp']
    b = cars['gear']
    c = cars['wt']
    data = list([a,b,c])

    # ploting the box
    plt.violinplot(data, showmeans=True, showextrema=True)
    plt.title("Box plot Demo")
    plt.grid(True)
    plt.show()

# createViolinplot()
createViolinPlotOnCar()