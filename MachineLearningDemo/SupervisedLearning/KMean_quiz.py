import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

df = pd.read_csv(r'MachineLearningDemo\SupervisedLearning/Live.csv')
# print(df)
# print(df.info())
print('Null values are : \n', df.isnull().sum())
print('Duplicated values : ', df.duplicated().sum())
print('Unique id : ', df['status_id'].nunique())

df = df.drop_duplicates()
print('Duplicated values after dropping : ', df.duplicated().sum())

# df[['status_published_date', 'status_published_time']] = df['status_published'].str.split(' ', expand=True)
# df['status_published_date'] = pd.to_datetime(df['status_published_date'])
# df['status_published_time'] = pd.to_datetime(df['status_published_time'], errors='coerce').dt.time
# print(df.info())

df.drop(columns=['Column1', 'Column2', 'Column3', 'Column4', 'status_published', 'status_id'], axis =1, inplace=True)
print(df.info())

for i in df.columns:
    if df[i].dtype != "onject":
        sns.boxplot(df[i])
        plt.title(i)
        # plt.show()

df_copy = df.copy()
df_copy.drop(['status_type'], axis =1, inplace=True)

se = StandardScaler()
df_scaled = se.fit_transform(df_copy)

df_scaled = pd.DataFrame(df_scaled, columns=df_copy.columns)
print(df_scaled)
print(df_scaled['num_reactions'].mean())
print(df_scaled['num_reactions'].std())

k_values = [2,3,4,5]
ssd = []

for k in k_values:
    km = KMeans(n_clusters=k, max_iter = 150, random_state = 32)
    km.fit(df_scaled)
    ssd.append(km.inertia_)

kmodel = KMeans(n_clusters=4, max_iter = 150, random_state = 32)
kmodel.fit(df_scaled)

print(kmodel.labels_)
df['clusterid'] = kmodel.labels_ #creating a new columns for these clusers
print(df)

group1 = df[df['clusterid'] == 1]
print(group1)

plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x = 'status_type', y = 'num_reactions', hue='clusterid', palette='Set1', s=150)
# plt.show()

hover_metrics = [
    "num_shares",
    "num_loves",
    "num_wows",
    "num_hahas",
    "num_sads",
    "num_angrys"
]

fig = px.scatter_3d(
    df,
    x="status_type",
    y="num_reactions",
    z="num_comments",
    color="clusterid",      # Color by cluster
    size="num_likes",       # Size of points by num_likes
    hover_name="status_type", # Display status type prominently on hover
    hover_data=hover_metrics, # Show all other engagement metrics on hover
    title="3D Scatter Plot: Engagement by Status Type and Cluster"
)
fig.update_layout(
    scene=dict(
        xaxis_title="Status Type",
        yaxis_title="Number of Reactions",
        zaxis_title="Number of Comments"
    ),
    width=900,  # Slightly wider for better view
    height=700
)
fig.show()
