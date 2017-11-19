from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
import numpy as np 
import sys

#load data
try:
    file = sys.argv[1]
    print(">Loading ", file, "....")
    data = np.genfromtxt(file, delimiter=',', skip_header=1)
    np.random.shuffle(data)
    x = data[:,1:]
    y = data[:,0]
    print(x.shape)
    print(y.shape)
    print("...............Done.................")
except IndexError:
    print("Need file name as argument")


def validate(pred, y):
	return np.sum(pred==y)/y.size*100

#Define SVR model:
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 0.1, 0.001, 10]}
svr = SVR()
clf = GridSearchCV(svr, parameters)

#Split data
s = int(y.size*4/5)
x_train = x[:s]
x_test = x[s:]
y_train = y[:s]
y_test = y[s:]



clf.fit(x_train, y_train)
print(clf.best_params_)

pred = clf.predict(x_test).astype(int)

print(y_test[:100], pred[:100])

print("Accuracy is ", validate(pred, y_test), "%.")