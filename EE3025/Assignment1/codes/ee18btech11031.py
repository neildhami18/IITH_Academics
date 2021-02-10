'''
Code by Neil
February 8, 2021
DSP Lab, Spring 2021
IIT Hyderabad
'''

import soundfile as sf
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

input_signal,fs = sf.read('Sound_Noise.wav')
sampl_freq=fs
order=4
cutoff_freq=4000.0
Wn=2*cutoff_freq/sampl_freq

#Parameters
num,den = signal.butter(order,Wn,'low')

#Filter the input signal with butterworth filter
output_signal = signal.filtfilt(num,den,input_signal)


#Filter application from scratch
def H(z,num,den):
    Num = np.polyval(num,z**(-1))
    Den = np.polyval(den,z**(-1))
    return Num/Den

def DigitalFilterApply(num,den,x):
    N = len(x)
    k = np.arange(N)
    w = 2*np.pi*k/N
    z = np.exp(1j*w)
    Hz = H(z,num,den)
    Xz = np.fft.fft(x)
    Yz = np.multiply(Hz,Xz)
    y = np.fft.ifft(Yz).real
    return y
    
output_signal_new = DigitalFilterApply(num,den,input_signal)

#write the output signal into .wav file
sf.write('Sound_With_ReducedNoise.wav',output_signal, fs)
sf.write('Sound_With_ReducedNoise_new.wav',output_signal_new, fs)

#Comparing outputs in time domain

plt.figure(1)
plt.figure(figsize=(8,7))
plt.suptitle("Time domain Comparison")
plt.subplot(2,1,1)
plt.plot(output_signal_new,'k')
plt.title('Designed Filter')
plt.grid()

plt.subplot(2,1,2)
plt.plot(output_signal,'r')
plt.title('In-built Filter')
plt.grid()

plt.savefig('ee18btech11031_1.eps')

# Comparing outputs in frequency domain

plt.figure(2)
plt.figure(figsize=(8,7))
plt.suptitle("Frequency Response Comparison")
plt.subplot(2,1,1)
plt.plot(np.abs(np.fft.fft(output_signal_new)),'k')
plt.title('Designed filter')
plt.grid()

plt.subplot(2,1,2)
plt.plot(np.abs(np.fft.fft(output_signal)),'r')
plt.title('In-built Filter')
plt.grid()

plt.savefig('ee18btech11031_2.eps')

#plt.show()

#If using termux
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11031_1.pdf"))
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11031_2.pdf"))


