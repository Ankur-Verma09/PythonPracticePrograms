import pandas as pd

class Filtering:
    @staticmethod
    def filter_by_gender():
        data = pd.read_csv('insurance.csv')
        print(data[data['sex'] == 'female'][['age', 'sex']])

    def condition_filter(self):
        data = pd.read_csv('insurance.csv')
        print(data[(data['smoker'] == 'yes') & (data['expenses'] > 20000)])


    condition_filter()