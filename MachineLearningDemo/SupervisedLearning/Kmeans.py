import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

df = pd.read_csv(r'MachineLearningDemo\SupervisedLearning\circket.csv', encoding='latin')
# print(df.head())
print(df.info())

df[['start','end']] = df['Span'].str.split('-', expand=True)
# print(df.head())
# print(df.info())

df['start'] = df['start'].astype(int)
df['end'] = df['end'].astype(int)
# print(df.info())

df['Exp'] = df['end'] - - df['start']
# print(df.head())

df.drop(columns=['Span','start','end'], axis=1, inplace=True)
# print(df.head())
# print(df.dtypes)

df['HS'] = df['HS'].str.replace('*',"")
df['HS'] = df['HS'].astype(int)
# print(df.info())

print(df.isnull().sum())
print(df.duplicated().sum())

for i in df.columns:
    if df[i].dtype != "onject":
        sns.boxplot(df[i])
        plt.title(i)
        # plt.show()

df_copy = df.copy()
df_copy.drop(['Player'], axis=1, inplace=True)

se = StandardScaler()
df_scaled = se.fit_transform(df_copy)
# print(df_scaled)

# Creating data frame from scaled values
df_scaled = pd.DataFrame(df_scaled, columns=df_copy.columns)
print(df_scaled)
print(df_scaled['50'].mean())
print(df_scaled['50'].std())

# How to choose the number of clusters
k_values = [2,3,4,5,6,7]
ssd = []

for k in k_values:
    km = KMeans(n_clusters=k, max_iter = 150, random_state = 32)
    km.fit(df_scaled)
    ssd.append(km.inertia_)

# plt.plot(k_values, ssd)

kmodel = KMeans(n_clusters=4, max_iter=150, random_state=32)
kmodel.fit(df_scaled)

print(kmodel.labels_)
df['clusterid'] = kmodel.labels_ #creating a new columns for these clusers
# print(df)

group1 = df[df['clusterid'] == 1]
# print(group1)

plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x = 'Runs', y = 'Ave', hue='clusterid', palette='Set1', s=150)
# plt.show()

fig = px.scatter_3d(df, x="Runs",y="Ave",z="SR",color ="clusterid",hover_name="Player",title="3d scatter plot")
fig.update_layout(scene=dict(xaxis_title="Runs",yaxis_title="Average",zaxis_title="strike rate"),width=800,height=600)
fig.show()
