"""
Read data:read data from different txt files, then write them into one
@aurthor Jiancheng Zeng
@April 30 2021

"""


import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy import array

"""
Select all the directories that contains data files
----------------------
"""
filenames = ["/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0000.dat", "/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0100.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0200.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0300.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0400.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0500.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0600.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0700.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0800.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_0900.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1000.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1100.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1200.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1300.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1400.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1500.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1600.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1700.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1800.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_1900.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_2000.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_2100.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_2200.dat","/Users/jiancheng/GAPS/GAPS_local/data/d20211119/h20211119_2300.dat",]


"""
Read temperature data and combine them in one list, then save it to one txt file
----------------------
"""
data = []
for file in filenames:
    data.extend(array(np.genfromtxt(file, skip_header=1, skip_footer=0, names=None, dtype=float, usecols = list(range(25,72)), delimiter=',')))
np.savetxt("/Users/jiancheng/GAPS/GAPS_local/output/read_data_20211119.txt", data, delimiter = " , ", fmt='%1.4g')
#print(type(data))  #check data type
print("finish reading data!")

"""
Read time and combine them in one list, then save it to one txt file
----------------------
"""
T = []
for file in filenames:
    T.extend(array(np.genfromtxt(file, skip_header=1, skip_footer=0, names=None, dtype=str, usecols = list(range(0,1)), delimiter=',')))
    #print(T)
    #data = data.extend(data_list)

#print(type(T)) #check time data type
np.savetxt("/Users/jiancheng/GAPS/GAPS_local/output/read_time_20211119.txt", T, delimiter = "\n", fmt = "%s")
print("finish reading time!")
