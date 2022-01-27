"""
Plot data: plot data that just been read
@aurthor Jiancheng Zeng
@April 30 2021

"""

import numpy as np
import matplotlib.pyplot as plt
import statistics
from numpy import array
from matplotlib.font_manager import FontProperties

"""
Select which RTDs to plot and name them
---------------------
"""
RTDn = [22] #single channel plot
#RTDn = list(range(1,48))  #plot RTD numbers
#RTDt = ["reservoir", "L1 Buttom", "L1 Middle", "L1 Top", "L6 Buttom", "L6 Middle", "L6 Top", "L12 Buttom", "L12 Middle", "L12 Top"]
#RTDt = ["Reservoir", "Frame1", "Frame2", "Frame3", "Radiator", "Radiator","Radiator","Radiator"]
STDEV = []  #standard deviation
n=0
#C = ['black', 'springgreen', 'forestgreen', 'darkgreen', 'lightcoral', 'indianred', 'brown', 'royalblue', 'blue', 'navy']  #customize plot color
#W = [1, 0.5, 0.5, 0.5, 1, 1, 1, 1.5, 1.5, 1.5] #customize linewidth

"""
Read data from total data file
--------------------
"""
data1 = np.genfromtxt("/home/jiancheng/GAPS/GAPS_local/output/read_data_20211222.txt", skip_footer=0, skip_header=0, names=None, delimiter = " , ")    #get temperature data
data2 = np.genfromtxt("/home/jiancheng/GAPS/GAPS_local/output/read_data_20220105.txt", skip_footer=0, skip_header=0, names=None, delimiter = " , ")    #get temperature data
data3 = np.genfromtxt("/home/jiancheng/GAPS/GAPS_local/output/read_data_20220112.txt", skip_footer=0, skip_header=0, names=None, delimiter = " , ")    #get temperature data
data4 = np.genfromtxt("/home/jiancheng/GAPS/GAPS_local/output/read_data_20220118.txt", skip_footer=0, skip_header=0, names=None, delimiter = " , ")    #get temperature data
data5 = np.genfromtxt("/home/jiancheng/GAPS/GAPS_local/output/read_data_20220125.txt", skip_footer=0, skip_header=0, names=None, delimiter = " , ")    #get temperature data

#T = np.genfromtxt("/home/jiancheng/GAPS/GAPS_local/output/read_time_20220125.txt", skip_footer=0, skip_header=0, names=None, delimiter = "\n")    #get time data


End = len(data1[:,0])    #identify end time
StartTime = 0  #choose start time
EndTime = 40000  #choose end time
#print(EndTime)

"""
making plot and calculate standard deviation for equilibrium state
----------------------
"""
"""
for i in RTDn:
    plt.plot(data[StartTime:EndTime, i-1],  label = RTDt[n], linewidth=0.8)
    #STDEV.append(statistics.stdev(data[10600:14600, i-1]))
    #print("stadard deviation for RTD",RTDn[n],RTDt[n]," is",STDEV[n],'degree C')
    n = n+1
"""

plt.plot(data1[32580:72580, 21],  label = "Dec 22, 2021", linewidth=0.8)
plt.plot(data2[StartTime:EndTime, 21],  label = "Jan 05, 2022", linewidth=0.8)
plt.plot(data3[StartTime:EndTime, 21],  label = "Jan 12, 2022", linewidth=0.8)
plt.plot(data4[StartTime:EndTime, 21],  label = "Jan 18, 2022", linewidth=0.8)
plt.plot(data5[StartTime:EndTime, 21],  label = "Jan 25, 2022", linewidth=0.8)

"""
Make legends and axis
-------------------
"""
plt.xlabel('time/s', fontsize=30)
plt.xticks(fontsize=30)
plt.ylabel('temperature/$^\circ C$', fontsize=30)
plt.yticks(fontsize=30)
#plt.ylim([-130, 30])
plt.title('Frame temperature of LN2 run test(Last five runs)', fontsize=30)
plt.grid(color='k', linestyle='--', linewidth=.1)
plt.legend(loc='lower left', prop={'size':20})
#plt.annotate("start reservoir heater", [0,0])
plt.show()
