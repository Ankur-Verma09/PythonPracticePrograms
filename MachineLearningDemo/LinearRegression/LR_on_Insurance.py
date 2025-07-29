# Introduction : Insurance premiums are determined by a magnitude of factors that influence the cost of coverage
# for the insurance company. We are going to construct a Linear Regression model capable of predicting insurance
# charges for new customers.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import *
import seaborn as sns

df = pd.read_csv(rs"MachineLearningDemo\LinearRegression\New_insurance_data.csv")
# df.info()
# print(df.head())
# print(df.tail())
# print(df.sample(5))
print(df.columns.values.tolist())

# DataAnalysis
# print(df.isnull().sum())
print(f'total number of null values in the data:', df.isnull().sum().sum())
P = (52/1338) * 100 #If number of null are more then 10% of the data, then we need to fill it else we can drop the rows.
# df.fillna(df[col]).mean() --> to fill the null data if total count is more then 10%
# print(P)
df.dropna(inplace=True)
df.shape
print(df.duplicated().sum())
# df.drop_duplicates(inplace=True)

# Outliers
for col in df.columns:
    if df[col].dtype != 'object':
        plt.boxplot(df[col])
        plt.title(col)
        # plt.show()

# print(df.describe())
Q1 = df.age.quantile(0.25)
Q3 = df.age.quantile(0.75)
IQR = Q3 - Q1
LL = Q1 - 1.5 * IQR
UL = Q3 + 1.5 * IQR
df = df[(df.age >= LL) & (df.age <= UL)]

Q1 = df.bmi.quantile(0.25)
Q3 = df.bmi.quantile(0.75)
IQR = Q3 - Q1
LL = Q1 - 1.5 * IQR
UL = Q3 + 1.5 * IQR
df = df[(df.bmi >= LL) & (df.bmi <= UL)]

Q1 = df.past_consultations.quantile(0.25)
Q3 = df.past_consultations.quantile(0.75)
IQR = Q3 - Q1
LL = Q1 - 1.5 * IQR
UL = Q3 + 1.5 * IQR
df = df[(df.past_consultations >= LL) & (df.past_consultations <= UL)]

Q1 = df.NUmber_of_past_hospitalizations.quantile(0.25)
Q3 = df.NUmber_of_past_hospitalizations.quantile(0.75)
IQR = Q3 - Q1
LL = Q1 - 1.5 * IQR
UL = Q3 + 1.5 * IQR
df = df[(df.NUmber_of_past_hospitalizations >= LL) & (df.NUmber_of_past_hospitalizations <= UL)]

Q1 = df.Anual_Salary.quantile(0.25)
Q3 = df.Anual_Salary.quantile(0.75)
IQR = Q3 - Q1
LL = Q1 - 1.5 * IQR
UL = Q3 + 1.5 * IQR
df = df[(df.Anual_Salary >= LL) & (df.Anual_Salary <= UL)]

for col in df.columns:
    if df[col].dtype != 'object':
        plt.boxplot(df[col])
        plt.title(col)
        # plt.show()


# print(df.shape)
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# print(df.iloc[151:153])
x = df.iloc[:, :-1] #independent variable
y = df['charges']
# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=0)
# print(y_train)
lr = LinearRegression()
lr.fit(x_train, y_train) #training the model
pred = lr.predict(x_test)
# print('predection value :', pred)
result = r2_score(y_test, pred)
print(result * 100)
sns.regplot(x=pred, y = y_test)
plt.title("Best fit line for Linear Regression model")
plt.show()