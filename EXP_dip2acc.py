# -*- coding: utf-8 -*-
#试验数据滤波；转换成速度、加速度
#试验数据格式：位移（时间必须为相同时间间隔，即采样频率恒定）
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
from scipy import signal
#导入数据

Fs=2560 #采样频率la
file = 'shuchu.TXT'    #第一列为数据y
fileout=file[0:14]+'lvbo.txt'
aa = np.loadtxt(file,skiprows=10)
#x_old = aa[:,0]  # 取第一列数据
y_old=aa # 取第二列数据
lin_aa=int(np.size(aa,0)*0.95)  #0.95为截取数据的比例
x_old=np.arange(0,lin_aa/Fs,1/Fs) # 根据采样频率生成时间数据
x=x_old[0:lin_aa]
y=y_old[0:lin_aa]/1000        # 取第一列数据，调整单位为m
plt.plot(x,y,label=str(Fs)+'Hz')
plt.legend()
plt.show()
#用已有数据
'''
x = np.linspace(0, 1.0, Fs+1)  #该数据采样频率Fs=2000
ylow = np.sin(2 * np.pi * 5 * x)
yhigh = np.sin(2 * np.pi * 50 * x)
y = ylow + yhigh
'''

#低通滤波
#这里假设采样频率为1000hz,信号本身最大的频率为500hz，要滤除10hz以上频率成分，即截至频率为10hz，则wn=2*10/1000=0.02
Fp=30  #截止频率 Hz
Wc=2*Fp/Fs
b, a = signal.butter(10, Wc, 'lowpass')#滤波阶数越高越好，但是计算时间会增大
y_fil = signal.filtfilt(b, a, y)#y为要过滤的信号

diff_x1 = np.diff(y_fil)/(1/Fs)#微分一次
diff_y_fil = signal.filtfilt(b, a, diff_x1)#y为要过滤的信号

diff_diff_x1 = np.diff(diff_y_fil)/(1/Fs)#微分一次
diff_diff_y_fil = signal.filtfilt(b, a, diff_diff_x1)#y为要过滤的信号
y_out=np.arange(0,int(len(y_fil)/20)/128,1/128)
for index in range (int(len(y_fil)/20)):
    y_out[index] = y_fil[index*20]
plt.plot(x,y,label='y')
plt.plot(x,y_fil,label='y-fil')
plt.legend()
plt.show()

plt.plot(x[0:-1],diff_y_fil,label='dy-fil')    #求完一次差分后数据长度会减少1
plt.legend()
plt.show()

plt.plot(x[0:-2],diff_diff_y_fil,label='ddy-fil')
plt.legend()
plt.show()
np.savetxt(fileout,y_out)
