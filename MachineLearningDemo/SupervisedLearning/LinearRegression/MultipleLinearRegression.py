import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

def multiple_linear_regression_model():
    dataset = pd.read_csv('boston.csv')
    # all columns except first (contains string) and last column in X object
    # Last columns from Y object

    X = pd.DataFrame(dataset.iloc[:,1:-1])
    Y = pd.DataFrame(dataset.iloc[:,-1])
    # train the model
    # 30% of the record will be in test set
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=5)
    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)
    regressor = LinearRegression()
    regressor.fit(X_train,Y_train)

    y_pred = regressor.predict(X_test)
    y_pred = pd.DataFrame(y_pred,columns=['Predicted'])
    print('Mean Absolute Error: ', metrics.mean_absolute_error(Y_test,y_pred))
    print('Mean Squared Error: ', metrics.mean_squared_error(Y_test, y_pred))
    print('Root Mean Squared Error: ', np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))




multiple_linear_regression_model()