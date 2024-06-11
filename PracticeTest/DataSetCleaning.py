import pandas as pd

# rename one coulumn name
def renameField():
    cars = pd.read_csv('cars.csv')
    car = cars.rename(columns={cars.columns[0]:'model_name'})
    print(car)

# rename multiple coulumn name
def renameFields():
    cars = pd.read_csv('cars.csv')
    car = cars.rename(columns={cars.columns[0]:'model_name', cars.columns[10]:'gear_box'})
    print(car)

# Fill the null value in mean of the column
def fillNullValue():
    cars = pd.read_csv('cars_null.csv')
    car = cars.gear.fillna(cars.gear.mean())
    print(car)

# Drop column
def dropColumn():
    cars = pd.read_csv('cars_null.csv')
    car = cars.drop(columns=['disp'])
    print(car)

# find corelation b/w to variables
def findCorelation():
    cars = pd.read_csv('customer_churn.csv')
    car = cars[['customerID','Churn']].corr()
    print(car)
##### Did not Work ######



findCorelation()
# dropColumn()
# renameFields()
# fillNullValue()