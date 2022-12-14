'''
用于对数据进行滤波，然后降采样 其中fs为采样频率，fs_filt为截止频率
'''
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from scipy import signal
mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号



def lowpass_filter(signal, cutoff_frequency, fs):
    # Design the filter
    order = 4
    nyq = 0.5 * fs
    normal_cutoff = cutoff_frequency / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)

    # Apply the filter to the signal
    filtered_signal = filtfilt(b, a, signal)

    return filtered_signal

fs=5120                     #采样频率
file='dandiaolan2#46.txt'
fileout=file[0:np.size(file)-5]+'in.txt'
fs_filt=33                  #截止频率
y=np.loadtxt(file,skiprows=3)
x=np.arange(0,np.size(y)/fs,1/fs)
filtered_y = lowpass_filter(y,fs_filt,fs)



factor = 40
y_downsampled = signal.resample(filtered_y, len(filtered_y) // factor)

x_downsampled=np.arange(0,np.size(y_downsampled)/fs*factor,1/fs*factor) 

i=0
data_max=max(y_downsampled[0:100])
for item in y_downsampled:
    i=i+1
    if(abs(y_downsampled[i])>abs(data_max)*1.05):
        break
    
    
y_out=y_downsampled[4000:5220]
plt.plot(x,y)
plt.plot(x,filtered_y)
plt.xlabel('时间（s）')   
plt.show()


plt.plot(x_downsampled,y_downsampled)
plt.xlabel('时间（s）')   
plt.show()

plt.plot(y_out)
plt.show()

np.savetxt(fileout,y_out)