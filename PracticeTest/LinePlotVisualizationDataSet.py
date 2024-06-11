import inline
import matplotlib
import numpy as np
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

def LinePlotEx():
    x = np.arange(0, 10, 0.1)
    y = 2*x + 5
    plt.plot(x,y)
    plt.show()

def LinePlotAddTitle():
    x = np.arange(0, 10, 0.1)
    y = 2*x + 5
    plt.plot(x,y)
    plt.title("Line plot Demo")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

def playWithLine():
    x = np.arange(0, 10, 1)
    y = 2*x + 5
    # Change plot size
    fig=plt.figure(figsize=(10,5))
    plt.plot(x,y, linestyle = ":", color = "red", alpha=0.5, marker = 'o')
    plt.title("Line plot Demo")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend(['line1'],loc = 'best')
    plt.show()

def combinePlotsUsingSubPlot():
    x = np.arange(0, 10, 1)
    y1 = 2 * x + 5
    y2 = 3 * x + 10

    # creating two plots in a figure
    plt.subplot(1,2,1)
    plt.plot(x, y1, linestyle=":", color="red", alpha=0.5, marker='o')
    plt.title("Graph1")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(x, y2, linestyle=":", color="red", alpha=0.5, marker='o')
    plt.title("Graph2")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()


combinePlotsUsingSubPlot()
# playWithLine()
# LinePlotAddTitle()
# LinePlotEx()
# combinePlotsInDia()
# combinePlots()
# drawMatplotWithName1()
# drawMatplotWithName()
# drawMatplotforDiabetes()
# drawMatplotForCars()

