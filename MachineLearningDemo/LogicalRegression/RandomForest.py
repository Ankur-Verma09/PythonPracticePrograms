import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

churn_data = pd.read_csv(r"MachineLearningDemo/LogicalRegression/customer_churn.csv")
# print(churn_data.info())
# print(churn_data.describe())
# print(churn_data.describe(include="O"))
# print(churn_data.isnull().sum())
# print(churn_data.duplicated().sum())
# print(churn_data.isnull().sum())
churn_data=churn_data.dropna()
# Remove customerID
churn_data.drop(columns=["customerID"],inplace=True)
# print(churn_data.info())

#unique()
#nunique()
#value_counts()
le=LabelEncoder()
col_list=[]

for i in churn_data.columns:
  if (churn_data[i].dtype=="object")&(i!="Churn"):
    col_list.append(i)

# print(col_list)
for i in col_list:
  churn_data[i]=le.fit_transform(churn_data[i])
# print(churn_data)

# We now divide the data into 2 parts ie independent and Dependent variables

x=churn_data.drop(columns=["Churn"])
y=churn_data["Churn"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
regressor = RandomForestClassifier(n_estimators=200)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
print(accuracy_score(y_test,y_pred)*100)

sns.boxplot()
