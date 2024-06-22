import array

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression


def implementLR():
    Y_train = np.array([0, 1000, 2000, 3000])
    X_train = np.array([0, 100, 200, 300])
    # print(f"x_train.shape = {X_train.shape}")
    # print(f"y_train.shape = {Y_train.shape}")
    m = len(X_train)
    print(f"Number of training examples are = {m}")

    i = 0 # change the i value to 1 to see (X_1, X_2)
    X_i = X_train[i]
    Y_i = Y_train[i]
    print(f"(x^({i}), y^({i})) = ({X_i},{Y_i})")

    plt.scatter(X_train, Y_train, marker='x', c='r')
    plt.title("Housing Prices")
    plt.ylabel('Price (in 1000s of dollars)')
    plt.xlabel('Size (1000 sqft)')
    plt.show()

    # w = Parameter weight
    # b = Parameter bais

    w = 100
    b = 100


def compute_model_output(x,w,b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb

    tmp_f_wb = compute_model_output(implementLR().X_train, w,b)

    # plot our model prediction
    plt.plot(implementLR().X_train,tmp_f_wb, c='b', label='Our Pridiction')

    # plot our data points
    plt.scatter(implementLR().X_train, implementLR().Y_train, maker='x', c='r', label='Actual Values')

    # Set the title
    plt.title("Housing Prices")
    # Set the y-axis label
    plt.ylabel('Price (in 1000s of dollars)')
    # Set the x-axis label
    plt.xlabel('Size (1000 sqft)')
    plt.legend()
    plt.show()

compute_model_output(implementLR().X_train, w,b)
# implementLR()