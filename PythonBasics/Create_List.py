import pandas as pd

class Create_List:
    @staticmethod
    def create_list():
        data = pd.read_csv('insurance.csv')
        list1 = []
        for number in range(0, len(data)):
            list1.append(number)
        print(list1[:10])
        print(list1[-10:])

    @staticmethod
    def add_new_column():
        data = pd.read_csv('insurance.csv')
        list1 = []
        for number in range(0, len(data)):
            list1.append(number)
        data['key'] = list1
        print(data.head())

    add_new_column()
