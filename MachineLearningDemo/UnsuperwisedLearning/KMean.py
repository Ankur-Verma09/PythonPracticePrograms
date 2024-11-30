# Create clusters based on the circketers performance

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px
from sklearn.metrics import silhouette_score

df = pd.read_csv('circket.csv', encoding='latin')
# print(df.info())

df[['start', 'end']] = df['Span'].str.split('-',expand=True)

df['start']=df['start'].astype(int)
df['end']=df['end'].astype(int)
# print(df.dtypes)

df['Exp']=df['end']-df['start']
# print(df['Exp'])

df.drop(columns=['Span','start','end'], axis=1, inplace=True)
# print(df.info())
# print(df.head())

df['HS'] = df['HS'].str.replace('*','')
df['HS']=df['HS'].astype((int))
# print(df.info())
# print(f'find nulls',df.isnull().sum())
print(f'Duplicate records',df.duplicated().sum())

for i in df.columns:
    if df[i].dtype != 'onject':
        sns.boxplot(df[i])
        plt.title(i)
        # plt.show()


# Standardization
df_copy = df.copy()
df_copy.drop(['Player'], axis=1, inplace=True)
# print(df_copy.head())

se = StandardScaler()
# Fitting the data into standaerd scaler
df_scaled = se.fit_transform(df_copy)
# print(df_scaled)

# Creating a data framce from standardized value
df_scaled = pd.DataFrame(df_scaled, columns=df_copy.columns)
# print(df_scaled)

k_value = [2,3,4,5,6,7]
ssd = []
for k in k_value:
    km = KMeans(n_clusters=k, max_iter=150, random_state=32)
    km.fit(df_scaled)
    ssd.append(km.inertia_)

# It measures how good the data points in the data set are clustered around the centriods
# ssd of each data point to its nearest cluster.

# plt.plot(k_value, ssd)
# plt.show()

kmodel = KMeans(n_clusters=4, max_iter=150, random_state=32)
kmodel.fit(df_scaled)

# print(kmodel.labels_)
# Creating a new columns for these lables
df['clusterId'] = kmodel.labels_
# print(df)

group1 = df[df['clusterId']==1]
# print(group1)
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Runs', y='Ave', hue='clusterId', palette='Set1', s=150)
# plt.show()

fig = px.scatter_3d(df, x='Runs', y='Ave', z = 'SR', color='clusterId', hover_name='Player', title='2d scatter plot')
fig.update_layout(scene=dict(xaxis_title='Runs', yaxis_title='Average', zaxis_title='strike rate'), width=800, height=500)
# fig.show()

k_values = range(2,8)
silhouette_scores=[]
for k in k_values:
  kmeans=KMeans(n_clusters=k,random_state=32)
  kmeans.fit(df_scaled)

  silhouette_avg=silhouette_score(df_scaled, kmeans.labels_)
  silhouette_scores.append(silhouette_avg)

plt.subplot(1,2,2)
plt.plot(k_values,silhouette_scores,marker='o',color='green')
plt.show()