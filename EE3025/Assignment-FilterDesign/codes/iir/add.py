import numpy as np


def add(x,y):
    '''
    This function adds two polynomials 
    defined by vectors x and y 
    z = add(x,y)
    '''
    m = len(x)
    n = len(y)
    
    if m == n:
        z = x + y
    elif m > n:
        z = x + np.concatenate((np.zeros(m-n),y))
    else:
        z = np.concatenate((np.zeros(n-m),x)) + y
        
    return z

    