import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")
# print(df.head())
# print(df.isnull().sum())
print(df.duplicated().sum())

# Outlier
for col in df.columns:
    if df[col].dtype != 'object':
        plt.boxplot(df[col])
        plt.title(col)
        # plt.show()

# price, bedrooms, bathrooms, sqft_living,sqft_lot,waterfront,view,condition,grade,
#  sqft_above,sqft_basement,yr_renovated,lat,long,sqft_living15,sqft_lot15

Q1 = df.price.quantile(0.25)
Q3 = df.price.quantile(0.75)
IQR = Q3-Q1
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.price>=LL) & (df.price<=UL)]

Q1 = df.bedrooms.quantile(0.25)
Q3 = df.bedrooms.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.bedrooms>=LL) & (df.bedrooms<=UL)]

Q1 = df.bathrooms.quantile(0.25)
Q3 = df.bathrooms.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.bathrooms>=LL) & (df.bathrooms<=UL)]

Q1 = df.sqft_living.quantile(0.25)
Q3 = df.sqft_living.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.sqft_living>=LL) & (df.sqft_living<=UL)]

Q1 = df.sqft_lot.quantile(0.25)
Q3 = df.sqft_lot.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.sqft_lot>=LL) & (df.sqft_lot<=UL)]

Q1 = df.waterfront.quantile(0.25)
Q3 = df.waterfront.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.waterfront>=LL) & (df.waterfront<=UL)]

Q1 = df.view.quantile(0.25)
Q3 = df.view.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.view>=LL) & (df.view<=UL)]

Q1 = df.condition.quantile(0.25)
Q3 = df.condition.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.condition>=LL) & (df.condition<=UL)]

Q1 = df.grade.quantile(0.25)
Q3 = df.grade.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.grade>=LL) & (df.grade<=UL)]

Q1 = df.sqft_above.quantile(0.25)
Q3 = df.sqft_above.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.sqft_above>=LL) & (df.sqft_above<=UL)]

Q1 = df.sqft_basement.quantile(0.25)
Q3 = df.sqft_basement.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.sqft_basement>=LL) & (df.sqft_basement<=UL)]

Q1 = df.yr_renovated.quantile(0.25)
Q3 = df.yr_renovated.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.yr_renovated>=LL) & (df.yr_renovated<=UL)]

Q1 = df.lat.quantile(0.25)
Q3 = df.lat.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.lat>=LL) & (df.lat<=UL)]

Q1 = df.long.quantile(0.25)
Q3 = df.long.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.long>=LL) & (df.long<=UL)]

Q1 = df.sqft_living15.quantile(0.25)
Q3 = df.sqft_living15.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.sqft_living15>=LL) & (df.sqft_living15<=UL)]

Q1 = df.sqft_lot15.quantile(0.25)
Q3 = df.sqft_lot15.quantile(0.75)
LL = Q1 - (1.5 * IQR)
UL = Q3 + (1.5 * IQR)
df = df[(df.sqft_lot15>=LL) & (df.sqft_lot15<=UL)]

for col in df.columns:
    if df[col].dtype != 'object':
        plt.boxplot(df[col])
        plt.title(col)
        # plt.show()

le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

x = df.iloc[:,:-1]
# print(x)
# y = df[]

