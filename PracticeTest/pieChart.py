import matplotlib.pyplot as plt
import pandas as pd

def createPieChart():
    movies = pd.read_csv('types_movies.csv')
    sectors = movies['Sector']
    percentage = movies['Percentage']

    # Creating a pie chart
    plt.pie(percentage, labels = sectors)
    plt.title('Pie Chart Demo')
    plt.show()


def customizePieChart():
    movies = pd.read_csv('types_movies.csv')
    sectors = movies['Sector']
    percentage = movies['Percentage']

    # Creating a pie chart
    plt.pie(percentage, labels = sectors, autopct='%1.1f%%', shadow=True, startangle=45)
    plt.title('Pie Chart Demo')
    plt.show()



customizePieChart()
# createPieChart()