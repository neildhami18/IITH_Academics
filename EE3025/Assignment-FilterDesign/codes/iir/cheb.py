import numpy as np

def cheb(N):
    '''
    THIS PROGRAM GENERATES 
    THE CHEBYSCHEV POLYNOMIAL 
    COEFFICIENTS OF ORDER N
    '''
    v = np.array([1,0])
    u = np.array([1])

    if N == 0:
        w = u
    
    elif N == 1:
        w = v
    
    else:
        for i in range(1,N):
            p = np.convolve(np.array([2,0]),v)
            m = len(p)
            n = len(u)
            w =  p + np.concatenate((np.zeros(m-n),u))
            u = v
            v = w
    
    return w