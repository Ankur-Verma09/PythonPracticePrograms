# You have access to the salary information of several employees along with their Years of
#  Experience. Using Linear regression analysis in machine learning, create a linear
#  regression model can predict the salary of an employee based on the years of
#  experience.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *
import seaborn as sns
import plotly.express as px

df =pd.read_csv(r"MachineLearningDemo\LinearRegression\data.csv")
print(df.columns.values.tolist()) #Print column names
print(f'total number of null values in the data:',df.isnull().sum())
print(df.shape)
print(f'Duplicate values: ', df.duplicated().sum())

# Outlier
for col in df.columns:
    if df[col].dtype != 'object':
        plt.boxplot(df[col])
        plt.title(col)
        # plt.show()

Q1 = df.YearsExperience.quantile(0.25)
Q3 = df.YearsExperience.quantile(0.75)
IQR = Q3-Q1
LL = Q1 - (1.5 * IQR)
UL = Q1 + (1.5 * IQR)
df = df[(df.YearsExperience >= LL) & (df.YearsExperience <= UL)]

Q1 = df.Salary.quantile(0.25)
Q3 = df.Salary.quantile(0.75)
IQR = Q3-Q1
LL = Q1 - (1.5 * IQR)
UL = Q1 + (1.5 * IQR)
df = df[(df.Salary >= LL) & (df.Salary <= UL)]

for col in df.columns:
    if df[col].dtype != 'object':
        plt.boxplot(df[col])
        plt.title(col)
        # plt.show()

# Label Encoding
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

x = df.iloc[:,:-1]
y = df['Salary']
# print(x)

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.20, random_state=0)
lr = LinearRegression()
lr.fit(x_train,y_train)

pred = lr.predict(x_test)
result = r2_score(y_test, pred)
print(result*100)
# sns.regplot(x = pred, y = y_test)
sns.displot(pred-y_test)
plt.title("Best fit line for Linear Regression model")
# plt.show()
plt.scatter(x_train, y_train)
plt.plot(x_train, lr.predict(x_train))
# plt.show()

a = float(input("Year of expirence: "))
features = np.array([[a]])
print("Predicted salary :", lr.predict(features))