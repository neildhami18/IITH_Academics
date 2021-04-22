#IIR  FILTER DESIGN USING THE CHEBYSCHEV APPROXIMATION

import numpy as np

from lp_stable_cheb import *
from lpbp import *
from bilin import * 
import matplotlib.pyplot as plt
import struct
#If using termux
import subprocess
import shlex
#end if


#The order of the filter is N = 4
N = 4
epsilon = 0.4
p,G_lp = lp_stable_cheb(epsilon,N)

# data imported from para.m file
Omega_0 = 0.4594043442925196
B = 0.09531188712133376
Omega_p1 = 0.5095254494944288
Omega_L = np.arange(-2,2+0.01,0.01)

#The analog lowpass filter
H_analog_lp = G_lp*np.abs(1.0/np.polyval(p,1j*Omega_L))
plt.figure(1)
plt.plot(Omega_L, H_analog_lp)
plt.grid()

#The analog bandpass filter
[num,den,G_bp] = lpbp(p,Omega_0,B,Omega_p1)
Omega = np.arange(-0.65,0.65+0.01,0.01) 
H_analog_bp = G_bp*np.abs(np.polyval(num,1j*Omega)/np.polyval(den,1j*Omega))
plt.figure(2)
plt.ylabel('$|H_{a,BP}(j\Omega)|$')
plt.xlabel('$\Omega$')
plt.plot(Omega,H_analog_bp)
plt.grid()
plt.savefig('../../figs/iir/AnalogBandpass.eps')
plt.savefig('../../figs/iir/AnalogBandpass.pdf')
#subprocess.run(shlex.split("termux-open ../../figs/iir/AnalogBandpass.pdf"))

#The Digital bandpass filter
dignum,digden,G = bilin(den,Omega_p1)
omega = np.arange(-2*np.pi/5,(np.pi/1000)+2*np.pi/5, (np.pi/1000))
H_dig_bp = G*np.abs(np.polyval(dignum,np.exp(-1j*omega))/np.polyval(digden,np.exp(-1j*omega)))
plt.figure(3)
plt.ylabel('$|H_{d,BP}(j\Omega)|$')
plt.xlabel('$\Omega$')
plt.plot(omega/np.pi,H_dig_bp)
plt.grid()
plt.savefig('../../figs/iir/DigitalBandpass.eps')
plt.savefig('../../figs/iir/DigitalBandpass.pdf')
#subprocess.run(shlex.split("termux-open ../../figs/iir/DigitalBandpass.pdf"))

plt.show()

iir_num = G*dignum
iir_den = digden
with open('dignum.dat', 'wb') as dat_file:  
    dat_file.write(struct.pack('f'*len(dignum), *dignum))


with open('digden.dat', 'wb') as dat_file:  
    dat_file.write(struct.pack('f'*len(digden), *digden))


with open('G.dat', 'wb') as dat_file:  
    dat_file.write(struct.pack('f', G))


with open('iir_num.dat', 'wb') as dat_file:  
    dat_file.write(struct.pack('f'*len(iir_num), *iir_num))


with open('iir_den.dat', 'wb') as dat_file:  
    dat_file.write(struct.pack('f'*len(iir_den), *iir_den))