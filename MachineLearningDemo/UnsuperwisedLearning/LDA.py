# LDA requires labels during training to -used for classification pblms -dimentionality reduction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report
import plotly.express as px

digits = load_digits()
digits.keys()
print(digits.keys())
# print(digits)
# print(digits.DESCR)
df = pd.DataFrame(digits.data, columns=digits.feature_names)
# print(df.head())
# print(df.to_string())
df['Target']=digits.target
# print(df.head())
plt.gray()
plt.matshow(digits.data[4].reshape(8,8))
plt.show()
#Independent
X=digits.data
#Dependent
Y=digits.target

# Training and Testing the data
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

# Standaardize the data
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# LDA
# In order to find the number of components for LDA wehave to use formula
# In case we have less number of features, min(No.Of Features, No. Of Classes) 
# min(n_classes-1, n_features)
# If we have 19 classes and 8 features, then (8, 19-1) = 8

# IN THIS DATA WE ARE HAVING 64 FEATURES NUMBER OF CLASS ARE 10
# SO MIN(64, 10-1) = 9
lda = LinearDiscriminantAnalysis(n_components=9)

# for training data use fit_transform
# for testinng data use transform
x_train = lda.fit_transform(x_train, y_train)
x_test = lda.transform(x_test)

# LDA Coefficients
x_train.shape
print(x_train.shape)
print(sum(lda.explained_variance_ratio_))
# Training the model
print(x_train.shape, x_test.shape)

model = RandomForestClassifier()
model.fit(x_train, y_train)
pred = model.predict(x_test)
print(accuracy_score(y_test, pred)*100)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

fig = px.scatter_3d(df, x=x_train[:,0], y=x_train[:,1],z=x_train[:,1], labels={'x':'LDA1', 'y':'LDA2', 'z':'LDA3'}, opacity=0.7, color=y_train)
fig.update_layout(scene=dict(xaxis_backgroundcolor="white",
                             yaxis_backgroundcolor="white",
                             zaxis_backgroundcolor="white"))

fig.update_layout(scene=dict(xaxis_showgrid=True, xaxis_gridwidth=1, xaxis_gridcolor='lightgrey',
                             xaxis_zeroline=True, xaxis_zerolinewidth=1, xaxis_zerolinecolor='lightgrey',
                             xaxis_showline=True, xaxis_linewidth=1, xaxis_linecolor='black',
                             yaxis_showgrid=True, yaxis_gridwidth=1, yaxis_gridcolor='lightgrey',
                             yaxis_zeroline=True, yaxis_zerolinewidth=1, yaxis_zerolinecolor='lightgrey',
                             yaxis_showline=True, yaxis_linewidth=1, yaxis_linecolor='black',
                             zaxis_showgrid=True, zaxis_gridwidth=1, zaxis_gridcolor='lightgrey',
                             zaxis_zeroline=True, zaxis_zerolinewidth=1, zaxis_zerolinecolor='lightgrey',
                             zaxis_showline=True, zaxis_linewidth=1, zaxis_linecolor='black'))

fig.update_layout(title_text="3D LDA Scatter Plot")
fig.update_traces(marker=dict(size=3))

fig.show()
