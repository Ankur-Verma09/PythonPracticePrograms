import pandas as pd

class Joins:
    @staticmethod
    def Inner_join():
        data = pd.read_csv('insurance.csv')
        list1 = []
        for number in range(0, len(data)):
            list1.append(number)
        data['key'] = list1
        defaulter = pd.read_csv('defaulter.csv')
        inner_df = pd.merge(data, defaulter, how = 'inner', left_on = 'key', right_on = 'key')
        print(inner_df)

    @staticmethod
    def left_join():
        data = pd.read_csv('insurance.csv')
        list1 = []
        for number in range(0, len(data)):
            list1.append(number)
        data['key'] = list1
        defaulter = pd.read_csv('defaulter.csv')
        inner_df = pd.merge(data, defaulter, how='left', left_on='key', right_on='key')
        print(inner_df)

    @staticmethod
    def left_join_selective_column():
        data = pd.read_csv('insurance.csv')
        list1 = []
        for number in range(0, len(data)):
            list1.append(number)
        data['key'] = list1
        defaulter = pd.read_csv('defaulter.csv')
        inner_df = pd.merge(data[['age', 'sex', 'key']], defaulter[['expenses', 'key']], how='left', left_on='key', right_on='key')
        print(inner_df)

    left_join_selective_column()