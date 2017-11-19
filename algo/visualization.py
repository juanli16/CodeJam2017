import sys 
import numpy as np 
import matplotlib.pyplot as p
import seaborn as sns
import pandas as pd

#Set general plot properties
sns.set_style("white")
sns.set_context({"figure.figsize": (24, 10)})

def loadData():
	#load data
	try:
	    file = sys.argv[1]
	    print(">Loading ", file, "....")
	    data = np.genfromtxt(file, delimiter=',', skip_header=1)
	    np.random.shuffle(data)
	    x = data[:,:2]
	    y = data[:,2:]
	    print(x.shape)
	    print(y.shape)
	    print("...............Done.................")
	except IndexError:
	    print("Need file name as argument")
	return x, y


x, y = loadData()

#Plot the number of trips per location ID:

location={}

for i in range(x.shape[0]):
	tmpx = x[i]
	location[int(tmpx[0])] = [0, 0]

for j in range(x.shape[0]):
	tmpx = x[j]
	tmpy = y[j]
	location[ int(tmpx[0]) ] = [sum(x) for x in zip ([ tmpy[0], tmpy[1] ], location[ int(tmpx[0]) ]) ]



locid, bikes = location.keys(), location.values()
bikes=  list(bikes)
locid = list(locid)

locid = np.array(locid)
bikes = np.array(bikes)

bikein = np.array(bikes)[:,0]
bikein = bikein/1000
bikeout = np.array(bikes)[:,1]
bikeout = bikeout/1000


df = pd.DataFrame(data = {'location':locid[:50], 'bikein':bikein[:50], 'bikeout':bikeout[:50]})

df2 = pd.melt(df, id_vars="location", var_name = "Bike flow", value_name = "Count (1000/month)")

print(df2.head())

#First plot
#top_plot = sns.barplot(x='location', y='bikein', color="#0000A3", data = df )
sns.factorplot(x="location", y="Count (1000/month)", hue="Bike flow", data=df2, kind='bar')


p.show()