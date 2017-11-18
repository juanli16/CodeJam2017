#!/usr/bin/python3

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

start = data['starttime']
start = start.values

stop = data['stoptime']
stop = stop.values

def convertTime(time):
    time_conv = []
    date_conv = []
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
        

        time_conv.append( sec + mins*60 + h*3600 )
        date_conv.append(date + month + year)

    return time_conv, date_conv

def split(data):
    starttime = data['starttime'].values
    stoptime = data['stoptime'].values
    startTime, startDate = convertTime(starttime)
    stopTime, stopDate = convertTime(stoptime)
    start = pd.DataFrame({'time': startTime, 'date': startDate, 'ID': data['start station id']})
    
    stop = pd.DataFrame({'time': stopTime, 'date': stopDate, 'ID': data['end station id']})
    
    return start, stop

print(convertTime(start[:2]))
print(convertTime(stop[:3]))
start, stop  = split(data)
print(start.head())
print(stop.head())
