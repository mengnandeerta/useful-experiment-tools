'''
用于对数据进行滤波，其中fs为采样频率，fs_filt为截止频率
'''
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
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
file='有水3#15.TXT'
fs_filt=10                  #截止频率
y=np.loadtxt(file,skiprows=3)
x=np.arange(0,np.size(y)/fs,1/fs)
filtered_y = lowpass_filter(y,fs_filt,fs)



plt.plot(x,y)
plt.xlabel('时间（s）')   
plt.show()


plt.plot(x,filtered_y)
plt.xlabel('时间（s）')   
plt.show()
