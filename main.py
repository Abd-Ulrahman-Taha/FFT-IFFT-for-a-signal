import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft , ifft


signal_rate, signal_data = wavfile.read("input.wav")
fft_data = np.fft.fft(signal_data)
fft_frequency = np.fft.fftfreq(len(fft_data)) * signal_rate
plt.figure(figsize=(10,6))
plt.plot(fft_frequency,np.abs(fft_data))
plt.xlabel('Frequency Hz')
plt.ylabel('Magnitude')
plt.title('Task-1 Using FFT')
plt.grid(True)
plt.show()

ifft_data = np.fft.irfft(fft_data)
ifft_data = np.round(ifft_data).astype('int16')
wavfile.write('OutPut.wav',signal_rate , ifft_data)

