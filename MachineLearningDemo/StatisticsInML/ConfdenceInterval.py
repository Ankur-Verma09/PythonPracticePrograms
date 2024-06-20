import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# Incomplete code

def confInterval():
    x = np.random.normal(100)
    sample_mean = np.mean(x)
    sample_std = np.std(x)
    std_err = st.sem(x)
    Z_value = st.norm.ppf(1 - 0.05)

    lowerCi = sample_mean - (Z_value * std_err)
    upperCi = sample_mean + (Z_value * std_err)

    # plotting Ci
    plt.figure(figsize=(15,5))
    # sns.distplot(x)
    plt.axvline(x=lowerCi, color='red')
    plt.axvline(x=upperCi, color='red')
    plt.axvline(x=sample_mean, color='green')
    plt.axvline(x=sample_std, color='green')
    plt.show()



confInterval()