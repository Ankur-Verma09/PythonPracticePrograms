import pandas as pd
data = pd.read_csv('defaulter.csv')

class AgeGroupping:
    @staticmethod
    def get_group_age():
        num = 0
        if num <= 18:
            return '0-18'
        elif num >18 and num <=30:
            return '19-30'
        elif num >30 and num <=45:
            return '31-45'
        else:
            return '45+'

        data['age_group'] = data['age'].map(AgeGroupping.get_group_age())
    print(data.head())

    get_group_age()
