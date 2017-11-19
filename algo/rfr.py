import sys 
import numpy as np 
from sklearn.ensemble import RandomForestRegressor as rfr 
from sklearn.metrics import mean_squared_log_error as msle
from sklearn.model_selection import KFold


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


model = rfr(n_estimators=300, criterion='mse', n_jobs=7, verbose=1)

kf = KFold(n_splits=5)

for train, test in kf.split(x):
	x_train, x_test = x[train], x[test]
	y_train, y_test = y[train], y[test]
	w = model.fit(x_train, y_train)
	print("Training Score is ", w.score(x_train, y_train))
	print("Testing Score is ", w.score(x_test, y_test))
	pred = w.predict(x_val)
	print("msle is ", msle(y_val, pred) )