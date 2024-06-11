import matplotlib.pyplot as plt
import pandas as pd


def createDoughnutChart():
    movies = pd.read_csv('types_movies.csv')
    sectors = movies['Sector']
    percentage = movies['Percentage']
    size_center = [5]
    # Creating a doughnut chart
    pie1 = plt.pie(percentage, labels=sectors, radius=1.5)
    pie2 = plt.pie(size_center, radius=1.0, colors= 'w')
    plt.title('Pie Chart Demo')
    plt.show()



def customizeDoughnutChart():
    movies = pd.read_csv('types_movies.csv')
    sectors = movies['Sector']
    percentage = movies['Percentage']
    size_center = [5]
    # a,b,c=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
    # Creating a doughnut chart
    pie1 = plt.pie(percentage, labels=sectors, radius=1.5)
    pie2 = plt.pie(size_center, radius=1.0, colors= 'w')
    plt.title('Pie Chart Demo')
    plt.show()


customizeDoughnutChart()
# createDoughnutChart()