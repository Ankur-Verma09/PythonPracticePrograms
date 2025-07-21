# Step1: Requirement Phase (Libraries)
# Confiiguration Libraries
import warnings
warnings.filterwarnings('ignore')

# Classical Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # not in use now days
plt.style.use('dark_background') # To create images with dard ackground

# Machine LLearning Libraries
import itertools
from sklearn.metrics import *

# Step2: Data Loading Phase (Data Ingestion)
# Data Loading

df = pd.read_csv('D:/Python/PythonPracticePrograms/MachineLearningDemo/UnsuperwisedLearning/AirPassengers.csv')
print(df.head())

# Shape inspection
a = df.shape
print(f'Rows: {a[0]}')
df.info()

# Insights
# The column months should be in date-time format
df['Month']= pd.to_datetime(df['Month'], infer_datetime_format=True)
print(df.head())

df = df.set_index('Month')
# plt.plot(df)
# plt.show

# Time series problem are always univariate
plt.figure(figsize=(8,5))
plt.show(df, color='red')
plt.show()

# The data shows the increasing trend moreover we can also say that this is a sessional upwards trend
# There is hude chance that the data might be un-stationary. By simply visulalizaing, since we canobserve

# Step3: Chec for stationality
# We need to ensure that the mean the variance is constant

# Rolling Statics
# Rolling mean
rolling_mean = df.rolling(window=12).mean  
