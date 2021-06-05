import sys
sys.path.insert(0, '..')

from utils import data
import os
import sklearn
import numpy as np
from sklearn.neighbors import (
    KNeighborsClassifier,
    DistanceMetric
)
import json

confirmed = os.path.join(
    '../COVID-19/csse_covid_19_data/', 
    'csse_covid_19_time_series',
    'time_series_covid19_confirmed_global.csv')
confirmed = np.loadtxt(open(confirmed), delimiter = ",", skiprows = 1, usecols=range(4, 502))
# Total dataset size is 276. Training set will be 221 (~80%), testing set will be 55.
testing_i = np.random.choice(confirmed.shape[0], size = 55, replace = False)
testing = confirmed[testing_i, :]
training = np.delete(confirmed, testing_i, axis = 0)
train_features = np.delete(training, -1, 1)
train_targets = training[:, -1]
test_features = np.delete(testing, -1, 1)
test_targets = testing[:, -1]

class LinearRegression():    
    def fit(self, features, targets):
        x = np.insert(features, 0, np.ones(features.shape[0]), axis = 1)
        self.weights = np.matmul(np.linalg.inv(np.matmul(x.T, x)), np.matmul(x.T, targets))

    def predict(self, features):
        predictions = np.empty(features.shape[0])
        x = np.insert(features, 0, np.ones(features.shape[0]), axis = 1)
        for i in range(0, x.shape[0]):
            predictions[i] = np.dot(x[i], self.weights)
        return predictions

    def visualize(self, features, targets):
        print("\nWeights: ", self.weights)
        print("\nX: ", features)
        print("\nY: ", targets)

model = LinearRegression()
model.fit(train_features, train_targets)
model.visualize(train_features, train_targets)
predictions = model.predict(test_features)
rmse = np.sqrt(np.mean((predictions-test_targets)**2))
print("\nRMSE: ", rmse)