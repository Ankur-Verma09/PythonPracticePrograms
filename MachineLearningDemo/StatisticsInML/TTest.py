from scipy import stats
from scipy.stats import t
import numpy as np

class TTest:
    @staticmethod
    def t_Test():
        population_mean = 100
        std_dev = 20
        sample_mean = 140
        n = 30
        ci = 95
        alpha=0.05 # or 1-ci

        # t_statistic
        t_stat = (sample_mean - population_mean) / (std_dev/np.sqrt(n))
        print(f't_stat: {t_stat}')

        # Degree of freedom
        df = n-1
        print(f'df: {df}')

        # t_critical value
        t_critical = t.ppf(1-0.05/2,df)  # ppf: percent point function
        print(f'T-critical: {t_critical}')

        # In manual problem solving we compare t_critical with t_stat to get the answer
        # but in code we comare p_value and alpha

        # Two ways of calculating p_value
        # method 1:
        p_value = 2 * (1- t.cdf(abs(t_stat), df))
        print(f'p_value: {p_value}')
        # method 2:
        # p_value = t.sf(abs(t_stat),df) * 2
        # print(f'p_value: {p_value}')

        if p_value < alpha:
            print('Reject Null hypo H0 : The mean is significantly different from pop')
        else:
            print('Accept Null hypo H0 : The mean is not significantly different from pop')


# Q: Suppose we do have two group of students: STudent from a school A and School B.
# We want to determine if there is a significant difference in their performcance on the standardized test

    @staticmethod
    def t_test_example():
        # generate data on your own
        alpha = 0.05
        school_a_score = np.random.normal(loc=75, scale=8, size=30) #mean scale = std dev
        school_b_score = np.random.normal(loc=70, scale=8, size=30)
        # print(school_a_score, school_b_score)

        t_statistic, p_value = stats.ttest_ind(school_a_score, school_b_score)
        print(f't_statistic: {t_statistic}')
        print(f'p_value: {p_value}')

        if p_value < alpha:
            print('Reject Null hypo H0 : The mean is significantly different in test score in A and B')
        else:
            print('Accept Null hypo H0 : The mean is not significantly different in test score in A and B')

    t_test_example()

