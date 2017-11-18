#!/usr/bin/python3

import pandas as pd
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as p

try:
    file = sys.argv[1]
    print("Processing ", file)
except IndexError:
    print("Need file name as argument")

#month dictionary:
m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


data = pd.read_csv(file)

start = data['starttime']
start = start.values

stop = data['stoptime']
stop = stop.values

def convertTime(time):
    time_conv = []
    #date_conv = []
    for i in range(len(time)):
        tmp = time[i]
        sec = int(tmp[17:19])
        mins = int(tmp[14:16])
        h = int(tmp[11:13])
        date  = int(tmp[8:10])      
        month = int(tmp[5:7])
        
        month = sum([m[i] for i in range(1,month)])
       
        year = (int(tmp[2:4])-14)
        if year%4==0:
            year = year * 366
        else:
            year = year * 365
       
        t = sec + mins*60 + h*3600
        d = date + month + year 
        
        total = t//3600 + d*24

        time_conv.append( total )
        #date_conv.append(d)

    return time_conv #, date_conv

def split(data):
    starttime = data['starttime'].values
    stoptime = data['stoptime'].values
    startTime = convertTime(starttime)
    stopTime = convertTime(stoptime)
    start = pd.DataFrame({'starttime': startTime, 'startID': data['start station id']})
    
    stop = pd.DataFrame({'stoptime': stopTime, 'stopID': data['end station id']})
    
    start = start.groupby(start.columns.tolist(), as_index=False ).size()
    stop = stop.groupby(stop.columns.tolist(), as_index=False ).size()
    return start, stop



print(convertTime(start[:2]))
print(convertTime(stop[:3]))
start, stop  = split(data)

df = pd.melt(start, id_vars= ['starttime'], value_vars=start.iloc[:,2], hue = ['startID'])

sns.barplot(x = id_vars, y = value_vars, hue = hue, data = df)

p.savefig("barplot.png")

print(start.head())
print(stop.head())
