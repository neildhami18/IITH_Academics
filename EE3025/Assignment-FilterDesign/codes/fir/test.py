import numpy as np
import matplotlib.pyplot as plt
import struct
#If using termux
import subprocess
import shlex
#end if

L = 114

#Sampling freqency (kHz)
Fs = 48

#Constant used to get the normalized digital freqencies
const = 2*np.pi/Fs

#The permissible filter amplitude deviation from unity
delta = 0.15

#Bandpass filter specifications (kHz)
#Passband F_p2 < F_p1
F_p1 = 3 + 0.6*(L-107)
F_p2 = 3 + 0.6*(L-109)

#Transition band
delF = 0.3

#Stopband F_s2 < F_p21; F_p1 < F_s1
F_s1 = F_p1 + 0.3
F_s2 = F_p2 - 0.3

#Normalized digital filter specifications (radians/sec)
omega_p1 = const*F_p1
omega_p2 = const*F_p2

omega_c = (omega_p1+omega_p2)/2
omega_l = (omega_p1-omega_p2)/2

omega_s1 = const*F_s1
omega_s2 = const*F_s2
delomega = 2*np.pi*delF/Fs


#The Kaiser window design
A = -20*np.log10(delta)
N = np.ceil((A-8)/(4.57*delomega))

N = 100
n = -np.arange(-N,N+1)#N:N
hlp = np.sin(n*omega_l)/(n*np.pi)
hlp[N] = omega_l/np.pi

#Bandpass filter
hbp = 2*hlp*np.cos(n*omega_c)

#lowpass filter 
omega = np.arange(-np.pi/2,np.pi/2+np.pi/200,np.pi/200)#-pi/2:pi/200:pi/2
Hlp = np.abs(np.polyval(hlp,np.exp(-1j*omega)))
plt.figure(1)
plt.plot(omega/np.pi,Hlp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{lp}(\omega)|$')
#plt.savefig('../../figs/fir/lowpass.pdf')
#plt.savefig('../../figs/fir/lowpass.eps')
subprocess.run(shlex.split("termux-open ../../figs/fir/lowpass.pdf"))
plt.grid()
#plt.show()



#bandpass filter 
omega = np.arange(-np.pi/2,np.pi/2+np.pi/200,np.pi/200)#-pi/2:pi/200:pi/2;

Hbp = np.abs(np.polyval(hbp,np.exp(-1j*omega)))
plt.figure(2)
plt.plot(omega/np.pi,Hbp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{bp}(\omega)|$')
#plt.savefig('../../figs/fir/bandpass.pdf')
#plt.savefig('../../figs/fir/bandpass.eps')
subprocess.run(shlex.split("termux-open ../../figs/fir/bandpass.pdf"))
plt.grid()
#plt.show()


fir_coeff = hbp

with open('fir_coeff.dat', 'wb') as dat_file:  
    dat_file.write(struct.pack('f'*len(fir_coeff), *fir_coeff))