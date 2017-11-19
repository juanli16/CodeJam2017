import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.advanced_activations import leakyRelu
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

def loadData():
	#load data
	try:
	    file = sys.argv[1]
	    print(">Loading ", file, "....")
	    data = np.genfromtxt(file, delimiter=',', skip_header=1)
	    x = data[:,1:]
	    y = data[:,0]
	    print(x.shape)
	    print(y.shape)
	    print("...............Done.................")
	except IndexError:
	    print("Need file name as argument")
	return x, y

def baseline_model():
	#Create model:
	model = Sequential()
	model.add(Dense(units = 64, input_shape=(2,)))
	model.add(LeakyReLU(alpha=0.3) )
	model.add(Dense(units = 1))
	
	#Compile model
	model.compile(loss='mean_squared_error', optimizart='adam')
	return model