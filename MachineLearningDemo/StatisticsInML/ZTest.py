import numpy as np
from scipy.stats import norm

class ZTest:
    # A shampoo manufacturing company manufacture a standand of 80ml of fluid in all Bottles, after getting a quick servicing of
    # their bottling machine they started bottling process again.A sample of 40 bottels were taken and it was found that the
    # avg weight of shampoo in sampled bottles is 70 ml, with a std dev of 2.5 ml, can we find out if there is a problem with the
    # bottling machine at CI-95 %
    @staticmethod
    def z_test_implementation():
        population_mean = 80
        sample_mean = 78
        pop_std_dev = 2.5
        n = 40
        alpha = 0.05

        # z_statistic
        z_stat = (sample_mean - population_mean) / (pop_std_dev/np.sqrt(n))
        print(f'z_stat: {z_stat}')

        # critical value
        z_critical_value = norm.ppf(1-alpha)
        print(f'z_critical_value: {z_critical_value}')

        #P-value
        p_value = 2 * (1-norm.cdf(abs(z_stat)))
        print(f'p_value: {p_value}')

        if p_value < alpha:
            print('Reject Null hypo H0 : There is significantly evidence machine is not working properly')
        else:
            print('Accept Null hypo H0 : There is significantly evidence machine is working properly')


    z_test_implementation()