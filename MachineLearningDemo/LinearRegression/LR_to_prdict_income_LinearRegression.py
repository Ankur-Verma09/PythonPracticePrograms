import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import *

df = pd.read_csv(f'MachineLearningDemo\LinearRegression\census-income .csv')
df.info()
# print(df.isnull().sum())
# print(df.duplicated().sum())
print("Before dropping the duplicates", df.shape)
df = df.drop_duplicates()
# print(df.duplicated().sum())
# print(df.isna().sum())
print("After dropping the duplicates", df.shape)
print('************')
df.info()

le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])
# print(df)

x = df.drop(columns=['annual_income'])
y = df['annual_income']
print(y)

# Fix train_test_split variable order
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# 6. (Optional) Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)
pred = model.predict(X_test_scaled)
print('R2 Score: ', r2_score(y_test, pred)*100)
