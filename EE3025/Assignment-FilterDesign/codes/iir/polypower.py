import numpy as np

def polypower(v,N):
    y = np.array([1])

    if N > 0:
        for i in range(1,N+1):
            y = np.convolve(y,v)
    return y
    