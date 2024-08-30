import pandas as pd

class Insurance:
    @staticmethod
    def insurance_method():
        data = pd.read_csv('insurance.csv')
        # print(data.head())
        # print(data.tail())
        print('Length of data file is: ', len(data))
        print(data.columns)
        print(data.info())

    @staticmethod
    def find_specific_data_using_indexing():
        data = pd.read_csv('insurance.csv')
        print(data.loc[0])
        print(data.loc[5:10])

    @staticmethod
    def find_perticular_column():
        data = pd.read_csv('insurance.csv')
        # print(data['age'])
        print(data['age'].head())

    @staticmethod
    def find_multiple_column():
        data = pd.read_csv('insurance.csv')
        # print(data['age'])
        print(data[['age', 'sex', 'region']].head())

    @staticmethod
    def findregision_wise_value():
        data = pd.read_csv('insurance.csv')
        # print(data['region'].value_counts())
        # print(data['region'].value_counts(normalize = True) *100)
        # print(data['smoker'].value_counts(normalize= True) * 100)
        print(data['sex'].value_counts(normalize=True) * 100)

    @staticmethod
    def avg_premium_at_region():
        data = pd.read_csv('insurance.csv')
        # select region, avg(charges) from data group by region
        # print(data.groupby(['region'])['expenses'].mean())
        # print(data.groupby(['sex'])['expenses'].mean())
        # print(data.groupby(['smoker'])['expenses'].mean())
        # print(data.groupby(['region', 'sex', 'smoker'])['expenses'].mean())
        print(data.groupby(['region', 'sex', 'smoker'])['expenses'].mean().reset_index())

    avg_premium_at_region()