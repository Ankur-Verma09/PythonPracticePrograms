import numpy as np
from scipy.stats import norm
from statsmodels.stats.proportion import proportions_ztest

# A survey was conducted in banglore, it was found that 960
# people out of 1860 were vegetrian and the rest were other
# food category group. Test that vegetrain and non-vegetrain are in
# equal proprotion at CI-99%

class ZTestForProportion:
    @staticmethod
    def z_test_Prop():
        alpha = 0.01
        veg_count = 960
        total_pop = 1860

        # phat
        p_hat = veg_count/total_pop

        z_stat, p_value = proportions_ztest(count=veg_count, nobs = total_pop, #number of observation)
                                            value= 0.50,
                                            alternative='two-sided')
        # critical value
        z_critical_value = norm.ppf(1 - alpha)
        print(f'z_critical_value: {z_critical_value}')

        if p_value < alpha:
            print('Reject Null hypo H0 : Veg and non-veg are unequal')
        else:
            print('Accept Null hypo H0 : Veg and non-veg are equal')



    z_test_Prop()