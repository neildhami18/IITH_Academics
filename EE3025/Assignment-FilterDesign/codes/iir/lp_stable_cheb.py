import numpy as np

def lp_stable_cheb(epsilon,N):
    '''
    %This function gives the low pass stable filter
    %for the Chebyschev approximation based upon
    %the design parameters epsilon and N
    %H(s) = G/p(s)
    %[p,G] = lp_stable_cheb(epsilon,N)

    %Analytically obtaining the roots of the Chebyschev polynomial
    %in the left half of the complex plane
    '''
    pi = np.pi
    beta = ((np.sqrt(1+epsilon**2)+ 1)/epsilon)**(1.0/N)
    r1 = (beta**2-1)/(2*beta)
    r2 = (beta**2+1)/(2*beta)
    '''
    %Obtaining the polynomial approximation for the low pass
    %Chebyschev filter to obtain a stable filter
    '''
    u = np.array([1])
    for n in range(int(N/2)):
        phi = pi/2 + np.divide((2*n+1)*pi,(2*N))
        v = np.array([1, -2*r1*np.cos(phi), r1**2*(np.cos(phi))**2+r2**2*(np.sin(phi))**2])
        p = np.convolve(v,u)
        u = p

    '''
    %Evaluating the gain of the stable lowpass filter
    %The gain has to be 1/sqrt(1+epsilon^2) at Omega = 1
    '''
    G = np.abs(np.polyval(p,1j))/np.sqrt(1+epsilon**2)
    #G = abs(polyval(p,j))
    return p,G