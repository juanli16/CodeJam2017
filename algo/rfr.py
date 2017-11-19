import sys 
import numpy as np 
from sklearn.ensemble import RandomForestRegressor as rfr 
from sklearn.metrics import mean_squared_log_error as msle
from sklearn.model_selection import KFold
import matplotlib.pyplot as p
import seaborn as sns

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
x_val = x[:1000]
y_val = y[:1000]

x = x[1000:]
y = y[1000:]


model = rfr(n_estimators=30, criterion='mse', n_jobs=16, verbose=1)

kf = KFold(n_splits=5)
d = {}
for train, test in kf.split(x):
	x_train, x_test = x[train], x[test]
	y_train, y_test = y[train], y[test]
	w = model.fit(x_train, y_train)
	pred_test = w.predict(x_test)
	m_test = msle(y_test, pred_test)
	print("msle for testing set is: ", m_test)
	pred = w.predict(x_val)
	#print(pred[:100], y_val[:100])
	m_val = msle(y_val, pred)
	print("msle for validation set is ", m_val )
	d[m_test*0.3 + m_val*0.7] = w


#Find the best tree:
best = d[ min(d.keys())]	
w = best.fit(x_train, y_train)
pred = w.predict(x_val)

df = pd.DataFrame({'x': y_val, 'y': pred})

fig = sns.regplot(x = 'x', y ='y', data=df, scatter=True) 
fig.savefig('scatter.png')
