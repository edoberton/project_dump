# Legendre polynomials 

# to reimplement using closure methods
import numpy as np
import matplotlib.pyplot as plt

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


x = np.linspace(-1, 1, 200)
# highest order of the polynomial
n = 8

polynomials = lp_generator(n,x)

for i in range(1, n+1):
    plt.plot(x, polynomials[i,:], label ="P "+str(i)) 
    plt.legend()

