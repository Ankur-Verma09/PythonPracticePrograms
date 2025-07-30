import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import PolynomialFeatures

# 1. Load and clean data
df = pd.read_csv('MachineLearningDemo/LinearRegression/census-income .csv')
df = df.drop_duplicates()
df = df.dropna()  # Optional: handle missing values

# 2. Encode categorical variables
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# 4. Define features and target
X = df.drop(columns=['annual_income'])
y = df['annual_income']
print(f'count of x: ', X)

# 5. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 6. (Optional) Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# # Create polynomial features (degree=2 is common, but you can try higher)
# poly = PolynomialFeatures(degree=2, include_bias=False)
# x_poly = poly.fit_transform(X)

# 7. Train Logistic Regression model
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train_scaled, y_train)
y_pred = logreg.predict(X_test_scaled)

# 8. Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred)*100)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, logreg.predict_proba(X_test_scaled)[:,1])*100)

user_input = []
for i in X:
    value = float(input(f'Enter value for {i}: '))
    user_input.append(value)

input_array = np.array(user_input).reshape(1, -1)
input_array_scaled = scaler.transform(input_array)
annual_income = logreg.predict(input_array_scaled)
print("Predicted: Income > 50K" if annual_income[0] == 1 else "Predicted: Income <= 50K")
