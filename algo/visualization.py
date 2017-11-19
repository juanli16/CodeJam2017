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

for i in range(x.shape[0]):
	tmpx = x[i]
	tmpy = y[i]
	location[int(tmpx[0])] = [tmpy[0], tmpy[1]] + location[int(tmpx[0])]

locid, bikes = location.items()
bikein = bikes[:,0]
bikeout = bikes[:,1]


df = pd.DataFrame(data = {'location':locid, 'bikein':bikein, 'bikeout':bikeout})

#First plot
top_plot = sns.barplot(x='location', y='bikein', color="#0000A3", data = df )

bottom_plot = sns.barplot(x='location', y='bikeout', color="#0000A3", data = df )

sns.despine(left=True)
bottom_plot.set_ylabel("Y-axis label")
bottom_plot.set_xlabel("X-axis label")

topbar = p.Rectangle((0,0),1,1,fc="red", edgecolor = 'none')
bottombar = p.Rectangle((0,0),1,1,fc='#0000A3',  edgecolor = 'none')
l = p.legend([bottombar, topbar], ['Bottom Bar', 'Top Bar'], loc=1, ncol = 2, prop={'size':16})
l.draw_frame(False)

#Set fonts to consistent 16pt size
for item in ([bottom_plot.xaxis.label, bottom_plot.yaxis.label] +
             bottom_plot.get_xticklabels() + bottom_plot.get_yticklabels()):
	item.set_fontsize(16)

p.show()