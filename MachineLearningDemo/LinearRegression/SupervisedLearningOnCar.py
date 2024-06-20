import pandas
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Various machine learning models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


def supervisedLeaningOnCar():
    data = pd.read_csv('customer_churn.csv')
    print(data.groupby('gender').size())
    array= data.values
    X=array[:,0:4]
    Y=array[0:4]
    validation_size=0.20
    seed=7
    scroing = 'accuracy'
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X,Y,test_size=validation_size,random_state=seed)


    # Building Models
    # spot check algorithms
    models = []
    models.append(('LR',LogisticRegression(solver='liblinear', multi_class='ovr')))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN',KNeighborsClassifier()))





supervisedLeaningOnCar()