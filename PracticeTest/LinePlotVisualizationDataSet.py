import inline
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt


# See how Hp varis with each car with line plot
def drawMatplotForCars():
    cars = pd.read_csv('cars.csv')
    y1 = cars['hp']
    x =  range(32)
    plt.plot(x,y1, color='pink')
    plt.show()

def drawMatplotforDiabetes():
    dia = pd.read_csv('diabetes.csv')
    y = dia['Glucose']
    x = range(768)
    plt.plot(x,y)
    plt.show()

def drawMatplotWithName():
    cars = pd.read_csv('cars.csv')
    y = cars['vs']
    x = range(32)
    plt.plot(x,y)
    plt.show()

def drawMatplotWithName1():
    cars = pd.read_csv('diabetes.csv')
    y = cars['Insulin']
    x = range(768)
    plt.plot(x,y)
    plt.show()

# Combine two plots
def combinePlots():
    cars = pd.read_csv('cars.csv')
    y1 = cars['wt']
    y2 = cars['drat']
    x = range(32)
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.show()


def combinePlotsInDia():
    dia = pd.read_csv('diabetes.csv')
    y1 = dia['Glucose']
    y2 = dia['BMI']
    x = range(768)
    plt.plot(x,y1)
    plt.plot(x, y2)
    plt.show()



# combinePlotsInDia()
combinePlots()
# drawMatplotWithName1()
# drawMatplotWithName()
# drawMatplotforDiabetes()
# drawMatplotForCars()

