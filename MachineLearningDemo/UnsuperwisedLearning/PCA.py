import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score


dataset = load_digits()
# print(dataset)
dataset.keys()
df = pd.DataFrame(dataset.data,columns=dataset.feature_names)
df['Target']=dataset.target
print('Target is',dataset.target[0]) # pixel values for image prsent at indext 0
dataset.data[0]
dataset.data[0].reshape(8,8)  # reshaping it by 8 *8 =64 pixel so it can form a image
plt.gray()
plt.matshow(dataset.data[0].reshape(8,8))
plt.show()

num_image = 5
plt.figure(figsize=(7,2))
for index in range(num_image):
    plt.subplot(1,5,index+1)
    plt.imshow(dataset.images[index], cmap = 'gray')
    plt.title(f'Label:{dataset.target[index]}')
    plt.axis('off')
plt.tight_layout()
plt.show()

df.shape
x = df.iloc[:,:-1] #deviding the data into dependent variable
y = dataset.target
y.shape

#Stand is useful to make components to be in same to calculatethe variance as well, to comapre wither it is important or not
scaler = StandardScaler()
X_scaled = scaler.fit_transform(x)
print(X_scaled)
print(pd.DataFrame(X_scaled))

#covariance = relation between two random variables and range from -infinity to +infinity
#corelation = Explains about the relations  between two variables and range from -1 to 1
# If the variablles are moving in the same direction then that is said to be postitive otherwise it is negative

x1 = X_scaled.T
print(pd.DataFrame(x1))
cov_matrix = np.cov(X_scaled.T)
print(pd.DataFrame(cov_matrix))

# EIGEN VALUES AND EIGEN VECTORS
# EIGEN VECTORS---DIRECTIONS IN WHICH THE DATA IS SPREAD OUT THE MOST Imagine you have a cloud of data points ,
#  eigen vectors tell you the most imp direction to look at where the data has the most VariableOffsetWindowIndexerin pca they represent the principal 
# components --the new axes along which we will project the data

# Eigen values---THE MAGNITUDE, THE IMPORATANCE
# tell us how much info(or variace) is captured along with the eigen vectors

eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
print(pd.DataFrame(eig_vals))
print(pd.DataFrame(eig_vecs))

tot = sum(eig_vals)
print(tot)

val_exp = [(i/tot) * 100 for i in sorted(eig_vals, reverse=True)]
print(val_exp)

# We do not need 0. It is not contributing to the variance. Hence removing it
# cumulative variance
cum_val_exp = np.cumsum(val_exp)
print(pd.DataFrame(cum_val_exp))

#screenplot(combination of bar and step plot)
plt.figure(figsize=(10,5))
plt.bar(range(len(val_exp)), val_exp, alpha=0.5, align='center', label='Individual explained variance')
plt.step(range(len(cum_val_exp)), cum_val_exp, label='cumulative explained variance')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.legend(loc='best')
plt.show()

# Apply PCA
pca=PCA(0.95)
X_pca = pca.fit_transform(X_scaled)
print(X_pca.shape)

# Model Building

x_train_pca,x_test_pca,y_train_pca,y_test=train_test_split(X_pca,y,test_size=0.2,random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(x_train_pca,y_train_pca)

#prediction
y_pred = model.predict(x_test_pca)
print(accuracy_score(y_test,y_pred)*100)