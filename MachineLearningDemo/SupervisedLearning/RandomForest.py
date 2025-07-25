import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'MachineLearningDemo/SupervisedLearning/customer_churn.csv')
# print(df)
print(f'shape: ', df.shape)
# print(f'head : ', df.head())

# df.duplicated() has 3 options:
#  keep=first, keep=last, keep=False
print(f'Duplicate values', df.duplicated().sum)
# print(f'info', df.info())
# print('Describe data \n', df.describe(include='O'))
print(f'Null values : \n', df.isnull().sum())

# Data encoding: to convert object type to required data type
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
print('TotalCharges are chnaged to required data type')

# errors='coerce' - Since we are forcefully changing the data type, if tehre are any special char in the data
# this param will be removing them

# print(f'Null values : \n', df.isnull().sum())
df = df.dropna()
print(f'Null values : \n', df.isnull().sum())

# drop customer id as it is not required and having alpha numeric
df.drop(columns=['customerID'], inplace=True)
print(df.info())

# for i in df.columns:
#     plt.boxplot(df[i])
#     plt.xlabel(i)
#     plt.show()

x = df.drop(columns=['Churn'])
print(x)
y = df['Churn']
print(y)

# x-train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.20, randome_state = 42)
