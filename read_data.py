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
filenames = ["../attach-txt-files/data/d20210720/h20210720_1300.dat", "../attach-txt-files/data/d20210720/h20210720_1400.dat", "../attach-txt-files/data/d20210720/h20210720_1500.dat", "../attach-txt-files/data/d20210720/h20210720_1600.dat", "../attach-txt-files/data/d20210720/h20210720_1700.dat", "../attach-txt-files/data/d20210720/h20210720_1800.dat", "../attach-txt-files/data/d20210720/h20210720_1900.dat", "../attach-txt-files/data/d20210720/h20210720_2000.dat", "../attach-txt-files/data/d20210720/h20210720_2100.dat", "../attach-txt-files/data/d20210720/h20210720_2200.dat", "../attach-txt-files/data/d20210720/h20210720_2300.dat"]


"""
Read temperature data and combine them in one list, then save it to one txt file
----------------------
"""
data = []
for file in filenames:
    data.extend(array(np.genfromtxt(file, skip_header=1, skip_footer=0, names=None, dtype=float, usecols = list(range(25,72)), delimiter=',')))
np.savetxt("../attach-txt-files/output/read_data_20210720.txt", data, delimiter = " , ", fmt='%1.4g')
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
np.savetxt("../attach-txt-files/output/read_time_20210720.txt", T, delimiter = "\n", fmt = "%s")
print("finish reading time!")
