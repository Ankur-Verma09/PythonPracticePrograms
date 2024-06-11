import pandas as pd

# cc.iloc[start from row : Ends with row, starts with column : Ends at columns]

# view customerID only
def viewSingleColumn():
    cc = pd.read_csv('customer_churn.csv')
    readonecolumn = cc.iloc[:,0]
    print(readonecolumn)


# this method will show first five columns of any row
def firstFiveColumn():
    cc = pd.read_csv('customer_churn.csv')
    firstfive = cc.iloc[0:5,1]
    print(firstfive)

# All the rows from all the columns
def allRowsOfColumns():
    cc = pd.read_csv('customer_churn.csv')
    allrows = cc.iloc[:,:]
    print(allrows)


# Find specific columns and limited columns
def readSpecificColumn():
    cc = pd.read_csv('customer_churn.csv')
    allrows = cc.iloc[:4,2:8]
    print(allrows)

def allRowsOfaColumn():
    cc = pd.read_csv('cars.csv')
    allrowsOfacolumn = cc.iloc[:,:1]
    print(allrowsOfacolumn)

def viewByAttributeName():
    cc = pd.read_csv('diabetes.csv')
    read = cc.loc[:,'BMI']
    print(read)

def viewByAttributeName():
    cc = pd.read_csv('diabetes.csv')
    read = cc.loc[:,'BMI']
    print(read)

def viewByAttributeFromToByName():
    cc = pd.read_csv('diabetes.csv')
    read = cc.loc[:6,'Pregnancies':'BMI']
    print(read)

def setValueInEntireColumn():
    dia = pd.read_csv('diabetes.csv')
    dia['Outcome'] = 1
    print(dia)

# Double up record using lamda function
def doubleYourValue():
    dia = pd.read_csv('diabetes.csv')
    f = lambda x:x*2;
    dia = dia['Outcome'].apply(f)
    print(dia)

def sortByAsc():
    dia = pd.read_csv('diabetes.csv')
    dia = dia.sort_values(by='Glucose')
    print(dia)

def sortByDesc():
    dia = pd.read_csv('diabetes.csv')
    dia = dia.sort_values(by='Glucose', ascending=False)
    print(dia)

# Filter the data with more than 120 glucose
def filterTheData():
    dia = pd.read_csv('diabetes.csv')
    result = dia['Glucose']>120
    print(result)


# Filter the data with more than 120 glucose and show the records
def filterTheDataAndShow():
    dia = pd.read_csv('diabetes.csv')
    result = dia['Glucose']>120
    result_new = dia[result]
    print(result_new)


# Filter the data with more than 120 glucose and BMI more than 26 show the records
def multipleFilterTheDataAndShow():
    dia = pd.read_csv('diabetes.csv')
    result = (dia['Glucose']>120) & (dia['BMI']>35)
    result_new = dia[result]
    print(result_new)





multipleFilterTheDataAndShow()
# filterTheDataAndShow()
# filterTheData()
# sortByDesc()
# doubleYourValue()
# setValueInEntireColumn()
# viewByAttributeFromToByName()
# viewByAttributeName()
# allRowsOfaColumn()
# readSpecificColumn()
# allRowsOfColumns()
# firstFiveColumn()
# viewSingleColumn()