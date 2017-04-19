# Models that are used during mockup

#### To run all the files / models
```
$ sudo python run_all.py
```

#### To run a single model:
```
$ sudo python <filename>.py
```
e.g., `sudo python model1.py`

The following output will be displayed:
```json
For 1 of 5 loops    Time taken: 0.498130083084  System time: 0.004  User time: 0.492    Memory used: 44810744
For 2 of 5 loops    Time taken: 0.509744167328  System time: 0.0    User time: 0.508    Memory used: 44813192
For 3 of 5 loops    Time taken: 0.469075918198  System time: 0.004  User time: 0.464    Memory used: 44813336
For 4 of 5 loops    Time taken: 0.502628803253  System time: 0.0    User time: 0.5  Memory used: 44813384
For 5 of 5 loops    Time taken: 0.485266923904  System time: 0.0    User time: 0.488    Memory used: 44813528
Accuracy: 97.037037037
Classification report for classifier SVC(C=1, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma=0.001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False):
             precision    recall  f1-score   support

          0       1.00      0.98      0.99        53
          1       0.96      1.00      0.98        53
          2       1.00      0.98      0.99        53
          3       0.96      0.89      0.92        53
          4       0.98      0.95      0.96        57
          5       0.95      0.98      0.96        56
          6       0.98      0.98      0.98        54
          7       1.00      1.00      1.00        54
          8       0.91      0.98      0.94        52
          9       0.96      0.96      0.96        55

avg / total       0.97      0.97      0.97       540

Confusion matrix:
[[52  0  0  0  1  0  0  0  0  0]
 [ 0 53  0  0  0  0  0  0  0  0]
 [ 0  0 52  1  0  0  0  0  0  0]
 [ 0  0  0 47  0  2  0  0  4  0]
 [ 0  0  0  0 54  0  0  0  1  2]
 [ 0  0  0  0  0 55  1  0  0  0]
 [ 0  1  0  0  0  0 53  0  0  0]
 [ 0  0  0  0  0  0  0 54  0  0]
 [ 0  1  0  0  0  0  0  0 51  0]
 [ 0  0  0  1  0  1  0  0  0 53]]

JSON
[
    {
        "f1": 0.9703011416825773,
        "params_dict": {
            "kernel": "'rbf'",
            "C": "1",
            "verbose": "False",
            "probability": "False",
            "degree": "3",
            "shrinking": "True",
            "max_iter": "-1",
            "decision_function_shape": "None",
            "random_state": "None",
            "tol": "0.001",
            "cache_size": "200",
            "coef0": "0.0",
            "gamma": "0.001",
            "class_weight": "None"
        },
        "recall": 0.9703703703703703,
        "precision": 0.9709883138208261,
        "params": "C=1, cache_size=200, class_weight=None, coef0=0.0,  decision_function_shape=None, degree=3, gamma=0.001, kernel='rbf',  max_iter=-1, probability=False, random_state=None, shrinking=True,  tol=0.001, verbose=False",
        "time": {
            "sys_time": {
                "average": 0.0015999999999999793,
                "worst": 0.0040000000000000036,
                "best": 0
            },
            "memory": {
                "average": 44812836.8,
                "worst": 44813528,
                "best": 44810744
            },
            "user_time": {
                "average": 0.49040000000000006,
                "worst": 0.508,
                "best": 0.4640000000000004
            },
            "time": {
                "average": 0.48460734803533556,
                "worst": 0.501382336209774,
                "best": 0.460714087079525
            }
        },
        "accuracy": 97.03703703703704
    }
]
```
