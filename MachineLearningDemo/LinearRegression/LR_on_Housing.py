import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import *
from sklearn.preprocessing import PolynomialFeatures
from datetime import date

df = pd.read_csv(r"MachineLearningDemo\LinearRegression\housing.csv")
# print(df.head())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.info())
# print(df.count())

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

# print(df.count())
print(f'Null Values: ', df.isnull().sum())
print(f'Duplicated Values: ', df.duplicated().sum())

# le = LabelEncoder()
# for col in df.columns:
#     if df[col].dtype == 'object':
#         df[col] = le.fit_transform(df[col])

# Creating new features that might have predictive power (e.g., house age = current year - yr_built).
current_year = date.today().year
df['house_age'] = current_year - df['yr_built']
df['years_since_renovation'] = current_year - df['yr_renovated']
df['years_since_renovation'] = df['years_since_renovation'].where(df['yr_renovated'] != 0, 0)

# Select the features you want to use (including engineered ones)
selected_features = [
    'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
    'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15',
    'house_age', 'years_since_renovation'
]
# x = df.drop(columns=['price', 'id', 'date'])
x= df[selected_features]
# print(x)
y = df['price']
# print(y)

# Create polynomial features (degree=2 is common, but you can try higher)
poly = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_poly, y , train_size = 0.80, random_state = 42)
model = LinearRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)
print('R2 Score is : ', r2_score(pred, y_test)*100)

# --- User input for all features ---
print("\nEnter the following values to predict the house price:")

user_input = []
for i in selected_features:
    value = float(input(f'Enter value for {i}: '))
    user_input.append(value)

input_array = np.array(user_input).reshape(1, -1)
input_array_poly = poly.transform(input_array)
predicted_price = model.predict(input_array_poly)
print("Predicted price of the house is :", predicted_price[0])
