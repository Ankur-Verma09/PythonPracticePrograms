import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import *
from sklearn import tree

df = pd.read_csv(r'MachineLearningDemo/SupervisedLearning/customer_churn.csv')
# print(df)
# print(f'shape: ', df.shape)
# print(f'head : ', df.head())

# df.duplicated() has 3 options:
#  keep=first, keep=last, keep=False
# print(f'Duplicate values', df.duplicated().sum)
# print(f'info', df.info())
# print('Describe data \n', df.describe(include='O'))
# print(f'Null values : \n', df.isnull().sum())

# Data encoding: to convert object type to required data type
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
# print('TotalCharges are chnaged to required data type')

# errors='coerce' - Since we are forcefully changing the data type, if tehre are any special char in the data
# this param will be removing them

# print(f'Null values : \n', df.isnull().sum())
df = df.dropna()
# print(f'Null values : \n', df.isnull().sum())

# drop customer id as it is not required and having alpha numeric
df.drop(columns=['customerID'], inplace=True)
# print(df.info())

# unique()
# nunique()
# value_counts()

# Label encoding --> It will directly assign some numbers value to the catagorical data
# 1 hot encoding -> If we are having less values STatus = (Single, Married, Enggaged) --> Can be done manually using math lib

le = LabelEncoder()
col_list=[]
for i in df.columns:
    if(df[i].dtype == "object")&(i!='Churn'):
        col_list.append(i)
# print(col_list)

# performing labelEncoding
for i in col_list:
    df[i]=le.fit_transform(df[i])
# print(df)

x = df.drop(columns=['Churn'])
# print(x)
y = df['Churn']
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.20, random_state=42)
model = DecisionTreeClassifier()
model2 = RandomForestClassifier(n_estimators=100)

parameters_to_try = {
    'random_state': [0,42,60,100],
    'max_depth':[1,5,50,100],
    'criterion': ['gini', 'entropy'],
    'min_samples_split':[2,6,8,10,5],
    'min_samples_leaf':[1,4,6,7,9]
}

gv = GridSearchCV(estimator=model, param_grid=parameters_to_try , cv = 3)
gv.fit(x_train, y_train)
print(gv.best_params_)
final_model = gv.best_estimator_
ans = final_model.predict(x_test)
print(accuracy_score(ans, y_test)*100)
tree.plot_tree(final_model, fontsize=7)

print('\n ****Random Forest result**** \n')
gv = GridSearchCV(estimator=model2, param_grid=parameters_to_try, cv = 3)
gv.fit(x_train, y_train)
print(gv.best_params_)
final_model2 = gv.best_estimator_
ans1 = final_model2.predict(x_test)
print(accuracy_score(ans1, y_test)*100)
estimator = final_model2.estimators_[0] #To print the first tree in the forest
# tree.plot_tree(final_model2, fontsize=7)
