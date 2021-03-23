'''
Code by Neil
March 23, 2021
DSP Lab, Spring 2021
IIT Hyderabad
'''

import soundfile as sf
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


input_signal,fs = sf.read('Sound_Noise.wav')
sampl_freq=fs
order=4
cutoff_freq=4000.0
Wn=2*cutoff_freq/sampl_freq

#Parameters
num,den = signal.butter(order,Wn,'low')


#Filter from scratch
def H(z,num,den):
    Num = np.polyval(num,z**(-1))
    Den = np.polyval(den,z**(-1))
    return Num/Den

def DigitalFilter(num,den,x):
    N = len(x)
    k = np.arange(N)
    w = 2*np.pi*k/N
    z = np.exp(1j*w)
    Hz = H(z,num,den)
    Xz = np.fft.fft(x)
    Yz = np.multiply(Hz,Xz)
    y = np.fft.ifft(Yz).real
    return y
    
output_signal_py = DigitalFilter(num,den,input_signal)

output_signal_c = np.loadtxt("../files/y.dat")
output_signal_c = output_signal_c[:,0]

#write the output signal into .wav file
sf.write('Sound_With_ReducedNoise_pyfft.wav',output_signal_py, fs)
sf.write('Sound_With_ReducedNoise_cfft.wav',output_signal_c[0:len(input_signal)],fs)


#Comparing outputs

plt.figure(1)
plt.figure(figsize=(8,7))
plt.suptitle("Output Comparison")
plt.subplot(2,1,1)
plt.plot(output_signal_py,'k')
plt.title('Python Built-in FFT Output')
plt.grid()

plt.subplot(2,1,2)
plt.plot(output_signal_c[0:len(input_signal)],'r')
plt.title("C-coded FFT Output")
plt.grid()

plt.savefig('../figs/ee18btech11031.eps')

#plt.show()

#If using termux
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11034_1.pdf"))
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11034_2.pdf"))