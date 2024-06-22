import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

def simpleReg():
    data = pd.read_csv('boston.csv')
    # print(data.head())
    # print(data.shape)
    # print(data.describe())
    data_ = data.loc[:,['INDUS', 'MEDV']]
    # print(data_.head(5))
    data.plot(x='INDUS',y='MEDV',style='o')
    plt.xlabel('INDUS')
    plt.ylabel('MEDV')
    # plt.show()
    X=pd.DataFrame(data['INDUS'])
    Y=pd.DataFrame(data['MEDV'])
    print(X.size), print(Y.size)

    # Train model
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2,random_state=1)
    # print(X_train.shape)
    # print(X_test.shape)
    # print(Y_train.shape)
    # print(Y_test.shape)
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    print(regressor.intercept_)
    print(regressor.coef_)
    y_pred = regressor.predict(X_test)
    y_pred = pd.DataFrame(y_pred, columns=['Predicted'])
    print('Mean Absolute Error: ', metrics.mean_absolute_error(Y_test,y_pred))
    print('Mean Squared Error: ', metrics.mean_squared_error(Y_test, y_pred))
    print('Root Mean squared Error: ', np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))





simpleReg()
