# CodeJam 2017: DataDive

This repository is for CodeJam 2017 DataDive. 
We are given the transportation data, which contained NewYork City 
2014 Bike traffic data, Uber, taxi and public transportation data. 

We focused on analyzing the bike traffic data, and we used also data from 2015, 2016 and 2017


## Model

## Feature 
We have built several Machine Learning regression models, in which the input features are **Time** (processed) and **location ID**, and the outputs are **Number of Bike in** and **Number of Bike out**. 

The Data set are binned in a time interval of 1 hour. 

The models we have tried includes linear regression, SVM regression, feed forward neural network, LSTM recurrent neural network, and finally Random Forest Regressions. 

### Metrics
The metrics to evaluate the model is MSLE: **Mean Squared Logarithm Error**

## Test/validate/split

We reserved 1000 data points for final validation purposes, and divided the dataset into 80:20 for all algorithms, into train/test sets.

## Results
Based on the MSLE metrics, Random Forest regression achieved the best result in the end with msle value 0f approximately 0.399.

A  subset of predicted output on the validation set of 2014 Bike traffic data is plotted with the actual values of the Bike traffic in 2014, in plot folder.

## How to run

To run the scripts, first preprocess the raw data by:
```Python3
pyhton3 timeconv.py datafilePath
```
Then to run any regression algorithms

```Python3
python3 algo.py processedfilePath
```
