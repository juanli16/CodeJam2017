#!usr/bin/python3

import pandas as pd
import numpy as np
import sys

try:
	file = sys.argv[1]
	print("Processing ", file)
except IndexError:
	print("Need file name as argument")

#month dictionary:
m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


data = pd.read_csv(file)

time = data['time']
time = time.values

time_conv = []
date_conv = []
for i in range(len(time)):
	tmp = time[i]
	sec = int(tmp[17:19])
	mins = int(tmp[14:16])
	h = int(tmp[11:13])
	date  = int(tmp[8:10])
	month = m[int(tmp[5:7])]
	year = int(tmp[0:4])-2014
	time_conv.append( sec + mins*60 + h*3600 )
	date_conv.append(date)
