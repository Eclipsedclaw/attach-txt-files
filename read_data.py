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
#filenames = ["/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0000.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0100.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0200.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0300.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0400.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0500.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0600.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0700.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0800.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0900.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1000.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1100.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1200.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1300.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1400.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1500.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1600.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1700.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1800.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1900.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_2000.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_2100.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_2200.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_2300.dat"]

filenames = ["/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0800.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_0900.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1000.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1100.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1200.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1300.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1400.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1500.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1600.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1700.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1800.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_1900.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_2000.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_2100.dat", "/home/jiancheng/GAPS/GAPS_local/data/d20211222/h20211222_2200.dat"]

"""
Read temperature data and combine them in one list, then save it to one txt file
----------------------
"""
data = []
for file in filenames:
    data.extend(array(np.genfromtxt(file, skip_header=1, skip_footer=0, names=None, dtype=float, usecols = list(range(25,73)), delimiter=',')))
np.savetxt("/home/jiancheng/GAPS/GAPS_local/output/read_data_20211222.txt", data, delimiter = " , ", fmt='%1.4g')
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
np.savetxt("/home/jiancheng/GAPS/GAPS_local/output/read_time_20211222.txt", T, delimiter = "\n", fmt = "%s")
print("finish reading time!")
