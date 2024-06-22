import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

def diabities():
    dataset = pd.read_csv('diabetes.csv')
    # print(dataset.head())
    # print(dataset.shape)
    # print(dataset['Outcome'].value_counts())
    sns.countplot(x='Outcome', data=dataset, palette = 'hls')
    # plt.show()
    x = pd.DataFrame(dataset.iloc[:,:-1])
    y = pd.DataFrame(dataset.iloc[:,-1])
    # print(x.head())
    # print(y.head())

    # Import train_test_split module to split dataset
    X_train, X_test, Y_Train, Y_test = train_test_split(x,y, test_size=0.3, random_state=1)
    logmodel = LogisticRegression()
    logmodel.fit(X_train, Y_Train)

    y_pred = logmodel.predict(X_test)
    print('Accuracy: %d', (logmodel.score(X_test, Y_test)))
    confusion_matrixs = confusion_matrix(Y_test, y_pred)
    print(confusion_matrixs)
    logit_roc_auc = roc_auc_score(Y_test, logmodel.predict(X_test))
    fpr, tpr, thresholds = roc_curve(Y_test, logmodel.predict(X_test)[:])
    plt.figure()
    plt.plot(fpr, tpr, label = 'Logistic Regression (area = %0.3f' %logit_roc_auc)
    plt.plot([0,1], [0,1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True positive Rate')
    plt.title('Receiver Operating Characteristics')
    plt.legend(loc='lower right')
    plt.savefig('Log_ROC')
    plt.show()



diabities()


