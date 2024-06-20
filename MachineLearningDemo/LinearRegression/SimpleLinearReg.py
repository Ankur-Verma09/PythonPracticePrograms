import matplotlib.pyplot as plt
import numpy as np

def estimate_coefficient(x,y):
    # size of dataset / number of observation points
    n = np.size(x)
    # calculate the mean of x and y
    mean_x, mean_y = np.mean(x), np.mean(y)
    # sum of square
    SS_xy = np.sum(y*x - n*mean_y*mean_x)
    SS_xx = np.sum(x*x - n*mean_x*mean_x)
    # regression coefficient : value at which the regression line needs to be move
    b1 = SS_xy / SS_xx
    b0 = mean_y - b1*mean_x
    return(b0,b1)

def plot_regression_line(x,y,b):
    plt.scatter(x,y, color = 'm', marker="o")
    # y predections
    y_pred = b[0]+b[1]*x
    plt.plot(x,y_pred, color= 'g')
    plt.xlabel('Size')
    plt.ylabel('Cost')
    plt.savefig('SimpleRegression')
    plt.show()

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([300,350,500,700,800,850,900,900,1000,1200])

b = estimate_coefficient(x,y)
print("Estimated Coefficient \nb0 = {} \nb1 = {}".format(b[0],b[1]))
# print("Estimated Coefficient \nb0 = ", b[0])
# print("Estimated Coefficient \nb1 = ",b[1])
plot_regression_line(x,y,b)