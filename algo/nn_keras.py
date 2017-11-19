import numpy as np
import pandas as pd
import sys
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN, TimeDistributed,  Dropout, Activation
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.recurrent import LSTM

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

def baseline_model():
	#Create model:
	model = Sequential()
	model.add(Dense(units = 16, input_shape=(2,), kernel_initializer='glorot_uniform' )) #, activation ='relu'))
	model.add(LeakyReLU(alpha=0.3) )
	model.add(Dense(units = 8 ) ) #activation='relu'))
	model.add(LeakyReLU(alpha=0.3) )
	model.add(Dense(units = 4))
	model.add(LeakyReLU(alpha=0.3) )
	model.add(Dense(units = 2))
	#Compile model
	#model.compile(loss='mean_squared_error', optimizer='adam')
	model.compile(loss='mse', # Mean squared error
                optimizer='rmsprop')
	return model


def rnn():
	model = Sequential()
	model.add(SimpleRNN(units = 64, input_dim=1, return_sequences=True))
	model.add(TimeDistributed(Dense(output_dim = 1, activation  =  "relu")))
	
	model.compile(loss = "mse", optimizer = "rmsprop")
	return model 

def lstm():
    model = Sequential()
    layers = [1, 64, 128, 256, 2]

    model.add(LSTM(
        layers[1],
        input_shape=(None, layers[0]),
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers[2],
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers[3],
        return_sequences=False))
    model.add(Dropout(0.2))
    
    model.add(Dense(
        layers[4]))
    model.add(Activation("linear"))

    model.compile(loss="mse", optimizer="rmsprop")
    return model

#load data:
x, y = loadData()
'''
s = int(y.size*4/5)
x_train = x[:s]
x_test = x[s:]
y_train = y[:s]
y_test = y[s:]
'''
x = x.reshape(x.shape[0], 2, 1)
#y = y.reshape(y.shape[0], 2, 1)

print(x[:10])
print(x.shape)

model = lstm()

print(model.summary())

model.fit(x, y, validation_split=0.2, batch_size=128, epochs=10, verbose=1)

#p = model.predict(x[:1000], batch_size=128, verbose = 1)

#p = [int(i) for i in p]
#print(p[:100], y[:100])

#np.random.seed(1337)

#sample_size = 256
#x_seed = [1, 0, 0, 0, 0, 0]
#y_seed = [1, 0.8, 0.6, 0, 0, 0]

#x_train = np.array([[x_seed] * sample_size]).reshape(sample_size,len(x_seed),1)
#y_train = np.array([[y_seed]*sample_size]).reshape(sample_size,len(y_seed),1)

#model=Sequential()
#model.add(SimpleRNN(input_dim  =  1, output_dim = 50, return_sequences = True))
#model.add(TimeDistributed(Dense(output_dim = 1, activation  =  "sigmoid")))
#model.compile(loss = "mse", optimizer = "rmsprop")

#model.fit(x_train, y_train, nb_epoch = 10, batch_size = 32)

#print(model.predict(np.array([[[1],[0],[0],[0],[0],[0]]])))