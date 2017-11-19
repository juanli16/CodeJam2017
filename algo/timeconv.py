#!/usr/bin/python3
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as p
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D

try:
    file = sys.argv[1]
    print("Processing ", file)
except IndexError:
    print("Need file name as argument")



def convertTime(time):
    time_conv = []
    #date_conv = []
    m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
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
    
    startID = data['start station id'].values
    start = [(i, j) for (i,j) in zip(startID, startTime)]
    startD = Counter(start)
    start = np.array([ [i, j, v] for (i,j), v in startD.items() ] )

    stopID = data['end station id'].values
    stop = [(i, j) for (i,j) in zip(stopID, stopTime)]
    stopD = Counter(stop)
    stop = np.array([ [i, j, v] for (i,j), v in stopD.items() ] )
    
    start = pd.DataFrame({'starttime': start[:,1], 'startID': start[:,0], 'count': start[:,2] } )
    stop = pd.DataFrame({'stoptime': stop[:,1], 'startID': stop[:,0], 'count': stop[:,2] } )
    #start = pd.DataFrame({'starttime': startTime, 'startID': data['start station id']})
    #stop = pd.DataFrame({'stoptime': stopTime, 'stopID': data['end station id']})
    
    #start = start.groupby(start.columns.tolist(), as_index=False ).size()
    #stop = stop.groupby(stop.columns.tolist(), as_index=False ).size()
    return start, stop



def plot3d(start):
    x = start['starttime'].values
    y = start['startID'].values
    z = start['count'].values

    fig = p.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.bar3d(x, y, z, 0.1, 0.1, 0.1)
    ax.set_xlabel('Start Time')
    ax.set_ylabel('Start ID')
    ax.set_zlabel('Count')

    p.savefig('3Dbarplot.png')


def saveDF(df, name):
    df.to_csv(name,sep=',',index=False,encoding='utf-8')

data = pd.read_csv(file)

start = data['starttime']
start = start.values

stop = data['stoptime']
stop = stop.values

#Preprocess data
start, stop  = split(data)

saveDF(start, "2014-04start.csv")
saveDF(stop, "2014-04stop.csv")


