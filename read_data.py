import csv
import matplotlib.pyplot as plt
import numpy as np
from numpy import array

"""
Select all the directories that contains data files
----------------------
"""
#filenames = ["/Users/jiancheng/GAPS/d20210504/h20210504_1000.dat","/Users/jiancheng/GAPS/d20210504/h20210504_1100.dat","/Users/jiancheng/GAPS/d20210504/h20210504_1200.dat","/Users/jiancheng/GAPS/d20210504/h20210504_1300.dat","/Users/jiancheng/GAPS/d20210504/h20210504_1400.dat","/Users/jiancheng/GAPS/d20210504/h20210504_1500.dat","/Users/jiancheng/GAPS/d20210504/h20210504_1600.dat"]
filenames = ["/users/jiancheng/gaps/d20210507/h20210507_1000.dat","/users/jiancheng/gaps/d20210507/h20210507_1100.dat","/users/jiancheng/gaps/d20210507/h20210507_1200.dat","/users/jiancheng/gaps/d20210507/h20210507_1300.dat","/users/jiancheng/gaps/d20210507/h20210507_1400.dat","/users/jiancheng/gaps/d20210507/h20210507_1500.dat"]

"""
Read temperature data and combine them in one list, then save it to one txt file
----------------------
"""
data = []
for file in filenames:
    data.extend(array(np.genfromtxt(file, skip_header=1, skip_footer=0, names=None, dtype=float, usecols = list(range(25,64)), delimiter=',')))
    #print(data)
    #data = data.extend(data_list)
np.savetxt("read_data_20210507.txt", data, delimiter = " , ", fmt='%1.4g')
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
np.savetxt("read_time_20210507.txt", T, delimiter = "\n", fmt = "%s")
print("finish reading time!")
