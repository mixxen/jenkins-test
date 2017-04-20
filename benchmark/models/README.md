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
For 1 of 5 loops    Time taken: 0.517853021622  System time: 0.008  User time: 0.512    Memory used: 44811136
For 2 of 5 loops    Time taken: 0.50639796257   System time: 0.0    User time: 0.504    Memory used: 44813584
For 3 of 5 loops    Time taken: 0.515566110611  System time: 0.004  User time: 0.508    Memory used: 44813728
For 4 of 5 loops    Time taken: 0.50090098381   System time: 0.0    User time: 0.5  Memory used: 44813776
For 5 of 5 loops    Time taken: 0.518049001694  System time: 0.004  User time: 0.512    Memory used: 44813920
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

RESPONSE
{
  "inputs": {
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
    "params": "C=1, cache_size=200, class_weight=None, coef0=0.0,  decision_function_shape=None, degree=3, gamma=0.001, kernel='rbf',  max_iter=-1, probability=False, random_state=None, shrinking=True,  tol=0.001, verbose=False"
  },
  "timeCreated": "2017-04-20 12:30:01.817390",
  "outputs": {
    "f1": 0.9703011416825773,
    "recall": 0.9703703703703703,
    "time": {
      "sys_time": {
        "average": 0.0032000000000000028,
        "worst": 0.008000000000000007,
        "best": 0
      },
      "memory": {
        "average": 44813228.8,
        "worst": 44813920,
        "best": 44811136
      },
      "user_time": {
        "average": 0.5072000000000002,
        "worst": 0.5120000000000005,
        "best": 0.5
      },
      "time": {
        "average": 0.5033915849432946,
        "worst": 0.5096871705756187,
        "best": 0.49253915269231796
      }
    },
    "precision": 0.9709883138208261,
    "accuracy": 97.03703703703704
  },
  "isPublic": false,
  "mid": "6606f9c7-1151-4808-911e-c36b1e7699af",
  "runCount": 0
}

[Finished in 11.5s]
```

Combined response of all the models
```json
{
  "model3": {
    "inputs": {
      "params_dict": null,
      "params": null
    },
    "timeCreated": "2017-04-20 12:33:05.643916",
    "outputs": {
      "accuracy": 82.5925925925926,
      "f1": 0.8288539138305351,
      "time": {
        "sys_time": {
          "average": 0,
          "worst": 0,
          "best": 0
        },
        "time": {
          "average": 0.0061484425124168395,
          "worst": 0.024734243939876555,
          "best": 0.0009367613091468812
        },
        "user_time": {
          "average": 0.011199999999999832,
          "worst": 0.03200000000000003,
          "best": 0.003999999999997783
        },
        "memory": {
          "average": 45005172.8,
          "worst": 45022024,
          "best": 44938704
        }
      },
      "precision": 0.8437668278950922,
      "recall": 0.825925925925926
    },
    "isPublic": false,
    "mid": "6606f9c7-1151-4808-911e-c36b1e7689af",
    "runCount": 0
  },
  "model2": {
    "inputs": {
      "params_dict": {
        "kernel": "'poly'",
        "C": "1",
        "verbose": "False",
        "degree": "3",
        "coef0": "0.0",
        "max_iter": "-1",
        "decision_function_shape": "None",
        "probability": "False",
        "random_state": "None",
        "tol": "0.001",
        "cache_size": "200",
        "shrinking": "True",
        "gamma": "0.001",
        "class_weight": "None"
      },
      "params": "C=1, cache_size=200, class_weight=None, coef0=0.0,  decision_function_shape=None, degree=3, gamma=0.001, kernel='poly',  max_iter=-1, probability=False, random_state=None, shrinking=True,  tol=0.001, verbose=False"
    },
    "timeCreated": "2017-04-20 12:33:02.499876",
    "outputs": {
      "accuracy": 94.81481481481482,
      "f1": 0.9481323096622317,
      "time": {
        "sys_time": {
          "average": 0,
          "worst": 0,
          "best": 0
        },
        "time": {
          "average": 0.14141214806890487,
          "worst": 0.16876409966802597,
          "best": 0.11947916467046737
        },
        "user_time": {
          "average": 0.14879999999999996,
          "worst": 0.17600000000000016,
          "best": 0.1280000000000001
        },
        "memory": {
          "average": 44910508.8,
          "worst": 44927304,
          "best": 44843984
        }
      },
      "precision": 0.9487044325727351,
      "recall": 0.9481481481481482
    },
    "isPublic": false,
    "mid": "6606f9c7-1151-4808-911e-c36b1e7658af",
    "runCount": 0
  },
  "model1": {
    "inputs": {
      "params_dict": {
        "kernel": "'rbf'",
        "C": "1",
        "verbose": "False",
        "degree": "3",
        "coef0": "0.0",
        "max_iter": "-1",
        "decision_function_shape": "None",
        "probability": "False",
        "random_state": "None",
        "tol": "0.001",
        "cache_size": "200",
        "shrinking": "True",
        "gamma": "0.001",
        "class_weight": "None"
      },
      "params": "C=1, cache_size=200, class_weight=None, coef0=0.0,  decision_function_shape=None, degree=3, gamma=0.001, kernel='rbf',  max_iter=-1, probability=False, random_state=None, shrinking=True,  tol=0.001, verbose=False"
    },
    "timeCreated": "2017-04-20 12:32:58.363642",
    "outputs": {
      "accuracy": 97.03703703703704,
      "f1": 0.9703011416825773,
      "time": {
        "sys_time": {
          "average": 0.002400000000000002,
          "worst": 0.0040000000000000036,
          "best": 0
        },
        "time": {
          "average": 0.4983779283270836,
          "worst": 0.5240511747107506,
          "best": 0.4571111055121422
        },
        "user_time": {
          "average": 0.5024,
          "worst": 0.5280000000000005,
          "best": 0.45999999999999996
        },
        "memory": {
          "average": 45065332.8,
          "worst": 45066024,
          "best": 45063240
        }
      },
      "precision": 0.9709883138208261,
      "recall": 0.9703703703703703
    },
    "isPublic": false,
    "mid": "6606f9c7-1151-4808-911e-c36b1e7699af",
    "runCount": 0
  }
}
```
