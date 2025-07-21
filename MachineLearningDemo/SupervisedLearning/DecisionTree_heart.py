import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import *
from sklearn import tree
from sklearn.model_selection import GridSearchCV


df = pd.read_csv(r'MachineLearningDemo\SupervisedLearning/heart.csv')
# print(df)
print(f'shape: ', df.shape)
print(f'Duplicate values are : ', df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(f'Duplicate values are : ', df.duplicated().sum())
print(f'shape: ', df.shape)
print(f'null values are : ', df.isnull().sum())
print(f'Info : ', df.info())

for i in df.columns:
    plt.boxplot(df[i])
    plt.xlabel(i)
    # plt.show()

x = df.drop(columns=['target'])
# print(x)
y = df['target']
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.20, random_state=3600)
model1 = DecisionTreeClassifier()
model1.fit(x_train, y_train)
y_pred = model1.predict(x_test)
# print(y_pred)

result = pd.DataFrame()
result['ActualResult'] = y_test
result['predicted value'] = y_pred
print(accuracy_score(y_test, y_pred)*100)
print(confusion_matrix(y_test, y_pred))
tree.plot_tree(model1, fontsize=7)
print(result.to_string())
# plt.show()

# create a new model to apply hyper parameter tuning on it
model2 = DecisionTreeClassifier()
parameters_t_try = {
    'random_state': [0,42,60,100,150,160,200,250,300],
    'max_depth':[1,5,50,100,120,150,180,200],
    'criterion': ['gini', 'entropy', 'logreg'],
    'min_samples_split':[2,6,8,10],
    'min_samples_leaf':[1,4,6,7,9,8]
}

gv = GridSearchCV(estimator=model2, param_grid=parameters_t_try , cv = 3)
gv.fit(x_train, y_train)
print(gv.best_params_) #returns best parameters for our model
final_model = gv.best_estimator_
ans = final_model.predict(x_test)
print(accuracy_score(ans, y_test)*100)
tree.plot_tree(final_model, fontsize=7)
plt.show()
