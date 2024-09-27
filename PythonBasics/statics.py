import sweetviz as sv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('country_profile_variables.csv')
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
class Statics:
    def imp_statics(self):
        data.isnull().sum().sum()
        # print(data['Population in thousands (2017)'].mean())
        # print(data['Population in thousands (2017)'].mode())
        # print(data['Population in thousands (2017)'].describe().round())
        # print(data.describe(include='O'))
        # print(data['Population in thousands (2017)'].count())
        # print(data['Population in thousands (2017)'].nunique())
        # print(data['Population in thousands (2017)'].unique())
        # print(data['country'].value_counts())
        # print(data['Population in thousands (2017)'].var())
        # # print(data['Population in thousands (2017)'].std().round(2))
        # print(np.percentile(data['Population in thousands (2017)'],50))

    def find_iqr(self):
        Q1 = data['Population in thousands (2017)'].quantile(0.25)
        Q2 = data['Population in thousands (2017)'].quantile(0.50)
        Q3 = data['Population in thousands (2017)'].quantile(0.75)
        IQR = Q3-Q1
        print('IQR is: ', IQR)
        UF = Q3+1.5*(IQR)
        LF = Q1-1.5*(IQR)
        print('Upper bound is: ', UF)
        print('Lower bound is: ', LF)
        print('max is: ', data['Population in thousands (2017)'].max())
        print('min is: ', data['Population in thousands (2017)'].min())
        sns.displot(data['Population in thousands (2017)'], kind='kde')
        sns.boxplot(data['Population in thousands (2017)'])
        plt.show()

        # How to create reports
        report = sv.analyze(data)
        report.show_html('polulation_record.html')




if __name__ == '__main__':
    statics = Statics()
    statics.find_iqr()