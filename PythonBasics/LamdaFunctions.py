import pandas as pd
data = pd.read_csv('defaulter.csv')
class LamdaFunctions:
    @staticmethod
    def lambda_function():
        data['child_upd_1'] = data['children'].apply(lambda x : x + 1)
        print(data.head())


    @staticmethod
    def lambda_if_condition():
        data['sex_flag'] = data['sex'].apply(lambda x : 0 if x == 'female' else 1)
        print(data.head())

    lambda_if_condition()