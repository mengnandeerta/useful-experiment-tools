# Example usage:
# Assuming a sampling frequency of 1000 Hz and a signal named 'signal_data'
# To plot the full spectrum, call the function without specifying x_axis_range:
# generate_fft_plot(1000, signal_data)

# To plot a specific x-axis range, provide the range as a tuple, e.g. (0, 200):
# generate_fft_plot(1000, signal_data, x_axis_range=(0, 200))

import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号

def generate_fft_plot(sampling_freq, signal, max_frequency):
    # Calculate the length of the signal
    signal_length = len(signal)
    
    # Calculate the FFT
    fft_result = np.fft.fft(signal)
    
    # Calculate the frequencies corresponding to FFT result
    frequencies = np.fft.fftfreq(signal_length, 1 / sampling_freq)
    
    # Take the absolute value of the FFT result to get the magnitude spectrum
    magnitude_spectrum = np.abs(fft_result)
    
    amplitude_spectrum = magnitude_spectrum*2/signal_length
    
    frequencies_truncated = frequencies[(frequencies >= 0) & (frequencies <= max_frequency)]
    amplitude_spectrum_truncated = amplitude_spectrum[(frequencies >= 0) & (frequencies <= max_frequency)]
    magnitude_spectrum_truncated = magnitude_spectrum[(frequencies >= 0) & (frequencies <= max_frequency)]
    return frequencies_truncated, amplitude_spectrum_truncated, magnitude_spectrum_truncated

signal_1 = np.loadtxt("moni.txt")
signal_2 = np.loadtxt('test.txt')
sampling_freq_1 = 182
sampling_freq_2 = 256

time_1 = np.arange(0, len(signal_1)) / sampling_freq_1
time_2 = np.arange(0, len(signal_2)) / sampling_freq_2

x_axis_range = 5

fre_s1,amp_s1,mag_moni = generate_fft_plot(sampling_freq_1,signal_1,x_axis_range)
fre_s2,amp_s2,mag_s2 = generate_fft_plot(sampling_freq_2,signal_2,x_axis_range)


plt.figure(figsize=(10, 5))
plt.plot(time_1, signal_1,label='moni')
plt.plot(time_2, signal_2,label= 'test')
plt.xlabel('Time(s)')
plt.ylabel('Y')
plt.title('Time-domin')

# Plot the magnitude spectrum
plt.figure(figsize=(10, 5))
plt.plot(fre_s1, mag_moni,label='moni')
plt.plot(fre_s2, mag_s2,label= 'test')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('FFT Magnitude Spectrum')
    



plt.figure(figsize=(10, 5))
plt.plot(fre_s1, amp_s1,label='moni')
plt.plot(fre_s2, amp_s2,label= 'test')
plt.xlabel('Frequency (Hz)')
plt.ylabel('AMP')
plt.title('FFT AMP Spectrum')
    


    
# plt.grid()
plt.legend()
plt.show()