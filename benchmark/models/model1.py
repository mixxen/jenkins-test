"""
model1.py

Model for predicting handwritten digits.

Classifier used: Support Vector Classifier
Kernel used: rbf

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

# To add the utilities directory in the sys.path
import os
utils_dir = os.path.dirname(os.path.dirname(__file__))

import sys

if os.path.isdir(utils_dir):
  sys.path.insert(0, utils_dir)
else:
  raise Exception('Utilities directory not found')

# Main program starts here
# Import the required libraries
from sklearn import (
    datasets,
    svm,
    metrics
)
import datetime
import warnings
warnings.filterwarnings("ignore")

from utilities.utils import (
    find_time,
    split_train_test
)

# Load the digits datasets
digits = datasets.load_digits()

# Flatten the 2D array to 1D array, 2d image to 1d array
# independent variable
X = digits.images.reshape((len(digits.images), -1))

# dependent variable
y = digits.target

# splits into 70% training and 30% testing
X_train, y_train, X_test, y_test = split_train_test(X, y, 0.7)

# Making the model, and passing few parameters
# Support Vector Classifier - RBF kernel
clf_rbf = svm.SVC(C=1, gamma=0.001, kernel='rbf')

# Fitting the model with training and testing data
clf_rbf.fit(X_train, y_train)


# To calculate the time taken
@find_time
def time_clf():
  clf_rbf.fit(X_train, y_train)

time_taken = time_clf()

# Getting the accuracy of the model
accuracy = clf_rbf.score(X_test, y_test) * 100
print 'Accuracy: {a}'.format(a=accuracy)
# The below one can also be used to calcualte the accuracy
# metrics.accuracy_score(expected, predicted)

# for making classification report
expected = y_test
predicted = clf_rbf.predict(X_test)

print("Classification report for classifier %s:\n%s"
      % (clf_rbf, metrics.classification_report(expected, predicted)))

print("Confusion matrix:\n%s"
      % metrics.confusion_matrix(expected, predicted))

# Converting to json
params = str(clf_rbf)
params_norm = params[params.find('(') + 1:params.find(')')].replace('\n', '')
params_dict = {
    k: v
    for k, v in [p.strip().split('=')
                 for p in params[params.find('(') + 1:params.find(')')]
                 .replace('\n', '')
                 .split(',')]
}

response = {
    "mid": "6606f9c7-1151-4808-911e-c36b1e7699af",
    'inputs': {
        'params': params_norm,
        'params_dict': params_dict,
    },
    'outputs': {
        'accuracy': accuracy,
        'precision': metrics.precision_score(expected, predicted),
        'recall': metrics.recall_score(expected, predicted),
        'f1': metrics.f1_score(expected, predicted),
        'time': time_taken,
    },
    "runCount": 0,
    "isPublic": False,
    "timeCreated": str(datetime.datetime.now()),
}


print
print 'RESPONSE'
print response
print
