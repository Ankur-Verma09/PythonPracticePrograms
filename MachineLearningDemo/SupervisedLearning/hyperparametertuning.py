import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import *
from sklearn import tree
from sklearn.model_selection import GridSearchCV


df = pd.read_csv(r'MachineLearningDemo/SupervisedLearning/heart_desease_data.csv')
# print(df)
print(f'shape : ', df.shape)
print(f'Duplicate values are : ', df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(f'Duplicate values are : ', df.duplicated().sum())
# print(f'Null values are : ', df.isnull().sum())
# print(f'Info : ', df.info())

for i in df.columns:
    plt.boxplot(df[i])
    plt.xlabel(i)
    # plt.show()

x = df.drop(columns=['target'])
# print(x)
y = df['target']
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.20, random_state=60)
model1 = DecisionTreeClassifier()
model1.fit(x_train, y_train)
y_pred = model1.predict(x_test)
# print(y_pred)

# create a df to compare actual and predected value
result = pd.DataFrame()
result['Actual value'] = y_test
result['predicted value'] = y_pred

# to print all the value from data frame
# print(result.to_string())
# print(f'shape : ', result.shape)

# check performance
print(accuracy_score(y_test, y_pred)*100)
# another way to check performance
print(confusion_matrix(y_test, y_pred))
tree.plot_tree(model1, fontsize=7)
# plt.show()

# create a new model to apply hyper parameter tuning on it
model2 = DecisionTreeClassifier()
# create a grid of all perameters that you want to try
parameters_to_try = {
   'random_state': [0,42,60,100],
    'max_depth':[1,5,50,100],
    'criterion': ['gini', 'entropy'],
    'min_samples_split':[2,6,8,10,5],
    'min_samples_leaf':[1,4,6,7,9]
}
# defallt values parameters_to_try
# Random state = 0, max_depth =8-10

gv = GridSearchCV(estimator=model2, param_grid=parameters_to_try , cv = 3)
# estimator = model on which you want to apply Hyper parameter tuning
# param_grid = Dict having all the parameters to be try
# cv = cross validation

# Train the model
gv.fit(x_train, y_train)
print(gv.best_params_) #returns best parameters for our model

# build a final model by using these best parameters
final_model = gv.best_estimator_

# Use final model for ptrdection
ans = final_model.predict(x_test)
print(accuracy_score(ans, y_test)*100)
tree.plot_tree(final_model, fontsize=7)
# plt.show()

