import numpy as np

def gauleg(lb, ub, nodes=128):
    
    # init
    prec = 1e-14
    x = np.full(nodes, 0.)
    w = np.full(nodes, 0.)

    m = int(nodes/2)

    xm = 0.5*(ub + lb)
    xl = 0.5*(ub - lb)

    z1 = 10e2

    z = np.cos(np.pi * (np.arange(m) +0.75)/(nodes + 0.5))
    while np.all(np.abs(z - z1) > prec):
        p1 = 1.
        p2 = 0.
        for j in range(nodes):
            p3 = p2
            p2 = p1
            p1 = ((2*j +1) * z * p2 - j * p3)/(j+1)
        
        pp = nodes*(z*p1 - p2)/(z**2 -1)
        z1 = z
        z = z1 - p1 / pp
    
    x[:m] = xm - xl *z
    x[m:] = xm + xl * np.flip(z)
    w[:m] = 2.0 * xl / ((1.0 - z**2) * pp * pp)
    w[m:] = np.flip(w[:m])
        
    return x, w
    
def gl_quadrature(f, lb, ub, nodes=128):
    
    # computation of quadrature weights and nodes
    x, w = gauleg(lb, ub, nodes)
    
    func_vec = w * f(x)
    return np.sum(func_vec)
    
    return 

def f(x):
    return np.exp(3*x) * x**2 + 0.5 * np.log(x)

int_sum = gl_quadrature(f, 0, 2)