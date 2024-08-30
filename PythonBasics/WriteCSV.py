import pandas as pd
data = pd.read_csv('defaulter.csv')
class WriteCSV:
    @staticmethod
    def write_to_csv():
        data['child_upd_1'] = data['children'].apply(lambda x : x + 1)
        data.to_csv('updated.csv')
        print(data.head())

    write_to_csv()
