"""
utility.py

Contains the list of utility functions.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""


def split_train_test(X, y, limit, *args, **kwargs):
    """
    Splits the vector and target to training and testing

    Splitting the datasets into training and testing, does a cross validation

    Returns X_train, y_train, X_test, y_test
    """

    if len(X) == len(y):
        n_samples = len(X)
    else:
        raise Exception('The lengths of X and y does not match')

    precent_of_sample = int(limit * n_samples)
    X_train = X[:precent_of_sample]
    y_train = y[:precent_of_sample]
    X_test = X[precent_of_sample:]
    y_test = y[precent_of_sample:]

    return X_train, y_train, X_test, y_test
