# -*- coding: utf-8 -*-
'''
Created on Tue Dec  6 11:53:33 2022

@author: zf
自谱分析程序，用于处理实验数据
'''


import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from scipy.signal import find_peaks
from scipy import signal

mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
mpl.rcParams['axes.unicode_minus']=False       #显示负号


file = '无水1#6.TXT'               #############################################################3#输入数据
Fs=5120                         #输入采样频率



x_start=1                       #跳过零周期                       
x_last=30                      #显示频率上限


data= np.loadtxt(file,skiprows=3)
#采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
data_max=max(data[0:1000])
data_min=min(data[0:1000])
dy=np.mean(data[np.size(data)-3000:np.size(data)])
data=data
i=0
for item in data:
    i=i+1
    if(abs(data[i])>abs(abs(data_max)+(data_max-data_min)*2)):
        break
data=data[i:np.size(data)]
x=np.arange(0,np.size(data)/Fs,1/Fs)         

y=data
 
fft_y=fft(y)                          #快速傅里叶变换
 
N=np.size(data)
Time=N/Fs
x_f=np.arange(0,Time,1.0/Fs)            # 频率个数

half_x = x_f[range(int(N/2))]  #取一半区间
k=np.arange(N)
fx=k/Time
half_fx=fx[range(int(N/2))]

abs_y=np.abs(fft_y)                # 取复数的绝对值，即复数的模(双边频谱)
angle_y=np.angle(fft_y)            #取复数的角度
normalization_y=abs_y/N            #归一化处理（双边频谱）                              
normalization_half_y = normalization_y[range(int(N/2))]      #由于对称性，只取一半区间（单边频谱）

x_plast=int(x_last/(half_fx[2]-half_fx[1]))
m=np.argmax(normalization_half_y[1:np.size(normalization_half_y)])

peaks, _ = find_peaks(data,prominence=0.1) # 寻峰
dT=round((peaks[int(np.size(peaks)*0.8)]-peaks[0])/Fs*fx[m])
ita=1/2/3.14/(dT)*np.log((data[peaks[0]]-dy)/(data[peaks[int(np.size(peaks)*0.8)]]-dy))*100
print('该试验时程的一阶频率为')
print(fx[m])
print('该试验时程的阻尼比为')
print(ita,'%')


plt.plot(x,y)   
plt.title('时程图')
plt.xlabel('时间（s）')
plt.ylabel('振幅（mm）')
plt.savefig("时程.jpg")
plt.show()

plt.plot(half_fx[x_start:x_plast],normalization_half_y[x_start:x_plast],label='归一化后频率曲线')
plt.title('频谱图')
plt.xlabel('频率（Hz）')
plt.ylabel('归一化幅值')
plt.legend()
plt.savefig("file.jpg")
plt.show()
 
