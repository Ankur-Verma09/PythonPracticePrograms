import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import *

# problem: Above data set past consist of customer data that has been given by bank. Now bank officials wants to launch a schema
# based on the past data we have to predict wether a person is gonna be interested in the scheme or not
# class LogicalRegression_banking:
df = pd.read_csv(r"MachineLearningDemo/LogicalRegression/bank-additional-full_final.csv")
    # print(df.describe())
    # print(df.info())

# EDA --> Explore Data Analysis
# 1. Null values
# 2. Duplicates
# 3. outliers
# 4. Label encod

    # print(df.isnull().sum())
df.isnull().sum()

# If we have null values
    # If have enough data --> drop the data using df.dropna(inplace = True)
# There is data scarcity --> replace null with mean for numerical and mode for categorical
#     for col in df.columns:
#         if(df[col].dtype != 'object'):
#             df[col].fillna(df[col].mean, inplace= True)
#         else:
#             df[col].fillna(df[col].mode(), inplace=True)

print('duplicate Values: ', df.duplicated().sum())
df.drop_duplicates(inplace=True)
print('duplicate Values: ', df.duplicated().sum())
print(df.shape)

# Outliers
for col in df.columns:
    if(df[col].dtype != 'object'):
        plt.boxplot(df [col])
        plt.xlabel(col)
            # plt.show()

    # print(df['pdays'].value_counts())
out_col = ['age', 'campaign', 'cons.conf.idx']
for col in out_col:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3-Q1
    LB = Q1 - (1.5*IQR)
    UB = Q3 + (1.5*IQR)

    df = df[(df[col]<= UB) & (df[col]>=LB)]
print(df.shape)

# Label Encoding
le = LabelEncoder()
for col in df.columns:
    if(df[col].dtype == 'object'):
        df[col]=le.fit_transform(df[col])
    # print(df.info())

# Eleminate the columns because all the columns are not required.
# Correlation
corelation_matrix = df.corr()
# print(corelation_matrix)

# Visualize the corelation
plt.figure(figsize=(16,10))
sns.heatmap(corelation_matrix, annot=True, cmap='coolwarm')
# plt.show()

# VIF --> Variation inflation factor (Will to calculate the scaler value for each column and find out the
# Multicolinarity.)
# Multicolinarity --> Columns of independent variables are interdepenedent on each other. We do not want

x=df.drop('y', axis=1)
y=df['y']
    # print(x)
    # print(y)
vif_df = pd.DataFrame() #Create an empty data frame
    # print(x.columns)
vif_df['feature'] = x.columns
    # print(vif_df)
vif_df["Multicollinearity"]=[variance_inflation_factor(x.values,i) for i in range(len(x.columns))]
    # print(vif_df)

x.drop('nr.employed',axis=1,inplace=True)
vif_df = pd.DataFrame()
vif_df['feature']  = x.columns
vif_df['Multicollinearity'] = [variance_inflation_factor(x.values, i) for i in range(len(x.columns))]
    # print(vif_df)

x.drop('cons.price.idx', axis=1, inplace=True)
vif_df = pd.DataFrame()
vif_df['feature'] = x.columns
vif_df['Multicollinearity'] = [variance_inflation_factor(x.values, i) for i in range(len(x.columns))]
    # print(vif_df)

x.drop('pdays', axis=1, inplace=True)
vif_df = pd.DataFrame()
vif_df['feature'] = x.columns
vif_df['Multicollinearity'] = [variance_inflation_factor(x.values, i) for i in range(len(x.columns))]
    # print(vif_df)

x.drop('euribor3m', axis=1, inplace=True)
vif_df = pd.DataFrame()
vif_df['feature'] = x.columns
vif_df['Multicollinearity'] = [variance_inflation_factor(x.values, i) for i in range(len(x.columns))]
    # print(vif_df)

x.drop('cons.conf.idx', axis=1, inplace=True)
vif_df = pd.DataFrame()
vif_df['feature'] = x.columns
vif_df['Multicollinearity'] = [variance_inflation_factor(x.values, i) for i in range(len(x.columns))]
    # print(vif_df)

x.drop('age', axis=1, inplace=True)
vif_df = pd.DataFrame()
vif_df['feature'] = x.columns
vif_df['Multicollinearity'] = [variance_inflation_factor(x.values, i) for i in range(len(x.columns))]
    # print(vif_df)

x.drop('poutcome', axis=1, inplace=True)
vif_df = pd.DataFrame()
vif_df['feature'] = x.columns
vif_df['Multicollinearity'] = [variance_inflation_factor(x.values, i) for i in range(len(x.columns))]
print(vif_df)

# Model Building
# 1. Data spliting --> Train and Test
# 2. Define the model
# 3. Train the model
# 4. Prediction
# 5. Evaluation

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.30)
lr = LogisticRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict(x_test)
print(accuracy_score(y_test,y_pred)*100)
cf = confusion_matrix(y_test, y_pred)
sns.heatmap(cf, annot=True, fmt='d',cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
precision_score(y_test, y_pred)
recall_score(y_test, y_pred)
print(classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)


