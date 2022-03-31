# Legendre polynomials 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def lp_init(x): 
        
    p_m2 = np.full(len(x), 1) # P0 = 1
    p_m1 = x # P1 = x
    
    np_pol = np.vstack((p_m2, p_m1)) 
    i = 2
    def lp_closure():
        nonlocal p_m1, p_m2, i, x, np_pol
        
        p = (((2 * i)-1)* x * p_m1 - (i-1)*p_m2)/float(i)
        np_pol = np.vstack((np_pol, p))
        
        p_m2 = p_m1
        p_m1 = p
        i += 1
        return i, np_pol
    
    return lp_closure


def lp_generator(n, x):
    
    if n == 0: return np.full(len(x), 1)
    if n == 1: return np.vstack((np.full(x.shape[0]), x)) 
    
    generator = lp_init(x)
    i = 2 
    while (i <= n):
        i, pol = generator()
        
    return pol

def polynomial_plot(n, x):

    polynomials = lp_generator(n,x)
    pol = pd.DataFrame(data=np.transpose(polynomials[1:, :]))
    pol.columns = ['deg. ' + str(i + 1) for i in range(len(pol.columns))]
    pol.index = x
    fig = plt.figure(figsize=(10,8)) # image size
    sns.lineplot(data=pol)
    # dashed grey line at 0
    sns.lineplot(y = np.zeros(len(x)), x = x, color='grey', linestyle='--')
    plt.show()


if __name__ == '__main__':
    x = np.linspace(-1, 1, 200)
    n = 4 # highest order of the polynomial

    # numpy matrix of polynomial values
    pol = lp_generator(n,x)
    # method to plot polynomials
    polynomial_plot(n,x)

