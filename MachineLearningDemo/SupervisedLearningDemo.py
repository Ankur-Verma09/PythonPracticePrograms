import pandas
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


def firstProgram():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pandas.read_csv(url, names=name)
    # print(dataset.shape)
    # Returns first 20 rows
    # print(dataset.head(20))

    # to return mean, min, count, std etc, we use describe
    # print(dataset.describe())

    # Described by class/ How many classes are there
    print(dataset.groupby('class').size())

    # unibariate: box and whisker plot
    # dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    # plt.show()

    # Create histrogram
    # dataset.hist()
    # plt.show()


    # Multi-varient: scatter plot matrix
    # scatter_matrix(dataset)
    # plt.show()

    # Creating a validation DataSet
    # Splitout validation data set - Dividing our dataset into train and test
    array = dataset.values
    X = array[:,0:4]
    Y = array[:,4]
    validation_size = 0.20  # slpit the data into 80-20 ration
    seed = 7 #initialize the randimoziation
    scoring = 'accuracy'
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X,Y,test_size=validation_size, random_state=seed)


    # Building Model
    # spot check algorithms
    models= []
    models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(gamma='auto')))

    # Evaluate each model in turn
    results = []
    names = []
    for name, model in models:
        kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)


    # Comparing Algorithms and select the best model
    # fig = plt.figure()
    # fig.suptitle('Algorithm Comparison')
    # ax = fig.add_subplot(111)
    # plt.boxplot(results,showmeans=True)
    # ax.set_xticklabels(names)
    # plt.show()


    # Make prediction on validation dataset
    svm = SVC(gamma='auto')
    svm.fit(X_train,Y_train)
    predictions = svm.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation,predictions))
    print(classification_report(Y_validation,predictions))

    knn = KNeighborsClassifier()
    knn.fit(X_train,Y_train)
    predictions = knn.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation,predictions))
    print(classification_report(Y_validation,predictions))



firstProgram()

