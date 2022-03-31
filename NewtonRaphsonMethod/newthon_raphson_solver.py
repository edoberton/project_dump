# problems of univariate solver:
# TODO: fix possible occurrence of infinite loop
# TODO: fix presence of more than one root
# improvements of the method:
# TODO: implement Newton-Raphson minimizer
# TODO: implement multivariate solver/minimizer
# github repo:
# TODO: write the documentation

import numpy as np

def fprime(f, x0, h=1e-5): # first derivative calculations
    return (f(x0 + h) - f(x0 - h))/(2*h)

# closure iteration allows for better memory allocation and computational efficiency
def newton_raphson(x, f): # closure function
    x0 = x
    
    def nr_closure():
        nonlocal x0, f 
        x0 = x0 - f(x0)/fprime(f, x0)
        return x0
    return nr_closure
    
def nr_solver(f, x, epsilon=1e-10): # main method
    
    solver = newton_raphson(x, f)
    x2 = x
    x1 = solver()
    while abs(x2 - x1) > epsilon:
        x1 = x2
        x2 = solver()
    return x2

if __name__ == '__main__':
    def f(x): # function to be solved
        # return x**3 - x - 1
        return x**2 + np.exp(x) -2

    sol = nr_solver(f, -5) # 5 = initial guess
    print(sol)

