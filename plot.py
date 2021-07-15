"""
Plot data: plot data that just been read
@aurthor Jiancheng Zeng
@April 30 2021

"""

import numpy as np
import matplotlib.pyplot as plt
import statistics
from numpy import array

"""
Select which RTDs to plot and name them
---------------------
"""
#RTDn = [17] #single channel plot
RTDn = list(range(1,20))  #plot RTD numbers
#RTDt = ["reservoir", "L1 Buttom", "L1 Middle", "L1 Top", "L6 Buttom", "L6 Middle", "L6 Top", "L12 Buttom", "L12 Middle", "L12 Top"]
STDEV = []  #standard deviation
n=0
#C = ['black', 'springgreen', 'forestgreen', 'darkgreen', 'lightcoral', 'indianred', 'brown', 'royalblue', 'blue', 'navy']  #customize plot color
#W = [1, 0.5, 0.5, 0.5, 1, 1, 1, 1.5, 1.5, 1.5] #customize linewidth

"""
Read data from total data file
--------------------
"""
data = np.genfromtxt("/Users/jiancheng/GAPS/read_data_20210507.txt", skip_footer=0, skip_header=0, names=None, delimiter = " , ")    #get temperature data
T = np.genfromtxt("/Users/jiancheng/GAPS/read_time_20210507.txt", skip_footer=0, skip_header=0, names=None, delimiter = "\n")    #get time data


End = len(data[:,0])    #identify end time
StartTime = 4050  #choose start time
EndTime = End  #choose end time
#print(EndTime)

"""
making plot and calculate standard deviation for equilibrium state
----------------------
"""
for i in RTDn:
    plt.plot(data[StartTime:EndTime, i-1],  label = 'RTD%d'%RTDn[n], linewidth=0.8)
    #STDEV.append(statistics.stdev(data[10600:14600, i-1]))
    #print("stadard deviation for RTD",RTDn[n],RTDt[n]," is",STDEV[n],'degree C')
    n = n+1



"""
Make legends and axis
-------------------
"""
plt.xlabel('time/s')
plt.ylabel('temperature/$^\circ C$')
#plt.ylim([-60, -20])
plt.title('Detectors RTD temperature')
plt.grid(color='k', linestyle='--', linewidth=.1)
plt.legend()
#plt.annotate("start reservoir heater", [0,0])
plt.show()
