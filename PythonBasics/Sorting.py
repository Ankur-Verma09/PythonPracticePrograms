import pandas as pd

class Sorting:
    @staticmethod
    def sorting():
        data = pd.read_csv('insurance.csv')
        grp_data = data.groupby(['region', 'sex', 'smoker'])['expenses'].mean()
        print(grp_data.sort_values(by = ['expenses']))

    @staticmethod
    def sorting_ascending():
        data = pd.read_csv('insurance.csv')
        grp_data = data.groupby(['region', 'sex', 'smoker'])['expenses'].mean()
        print(grp_data.sort_values(by = ['expenses']), ascending = True)

    @staticmethod
    def sorting_descending():
        data = pd.read_csv('insurance.csv')
        grp_data = data.groupby(['region', 'sex', 'smoker'])['expenses'].mean()
        print(grp_data.sort_values(by = ['expenses']), ascending = False)

    @staticmethod
    # modify actual dataframe
    def sorting_implace():
        data = pd.read_csv('insurance.csv')
        grp_data = data.groupby(['region', 'sex', 'smoker'])['expenses'].mean()
        print(grp_data.sort_values(by=['expenses']), implcase =True)

    sorting_implace()