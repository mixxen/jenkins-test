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
    "timeCreated": "2017-04-21 14:09:03.169001",
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
          "average": 0.0017426161065101625,
          "worst": 0.002906814028263092,
          "best": 0.0004756597771644593
        },
        "user_time": {
          "average": 0.007200000000000273,
          "worst": 0.008000000000002672,
          "best": 0.004000000000001336
        },
        "memory": {
          "average": 45005350.4,
          "worst": 45022184,
          "best": 44938864
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
    "timeCreated": "2017-04-21 14:08:59.580687",
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
          "average": 0.1489249559149742,
          "worst": 0.19848822076177597,
          "best": 0.12203811127996445
        },
        "user_time": {
          "average": 0.15839999999999996,
          "worst": 0.20800000000000018,
          "best": 0.13199999999999967
        },
        "memory": {
          "average": 44910668.8,
          "worst": 44927464,
          "best": 44844144
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
    "timeCreated": "2017-04-21 14:08:55.114691",
    "outputs": {
      "accuracy": 97.03703703703704,
      "f1": 0.9703011416825773,
      "time": {
        "sys_time": {
          "average": 0.0008000000000000007,
          "worst": 0.0040000000000000036,
          "best": 0
        },
        "time": {
          "average": 0.5586233468756676,
          "worst": 0.6245331617102623,
          "best": 0.506744131635189
        },
        "user_time": {
          "average": 0.5655999999999997,
          "worst": 0.6319999999999997,
          "best": 0.516
        },
        "memory": {
          "average": 45065492.8,
          "worst": 45066184,
          "best": 45063400
        }
      },
      "precision": 0.9709883138208261,
      "recall": 0.9703703703703703
    },
    "isPublic": false,
    "mid": "6606f9c7-1151-4808-911e-c36b1e7699af",
    "runCount": 0
  },
  "model4": {
    "inputs": {
      "params_dict": {
        "binarize": "0.0",
        "alpha": "1.0",
        "fit_prior": "True",
        "class_prior": "None"
      },
      "params": "alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True"
    },
    "timeCreated": "2017-04-21 14:09:06.722085",
    "outputs": {
      "accuracy": 82.5925925925926,
      "f1": 0.8268448952896597,
      "time": {
        "sys_time": {
          "average": 0,
          "worst": 0,
          "best": 0
        },
        "time": {
          "average": 0.0026445000227928164,
          "worst": 0.0032198576226234437,
          "best": 0.0021221490607261657
        },
        "user_time": {
          "average": 0.006399999999999295,
          "worst": 0.008000000000002672,
          "best": 0.003999999999997783
        },
        "memory": {
          "average": 45019684.8,
          "worst": 45036480,
          "best": 44953160
        }
      },
      "precision": 0.8354838760983377,
      "recall": 0.825925925925926
    },
    "isPublic": false,
    "mid": "6606f9c7-1151-4808-911e-c36b1e7459af",
    "runCount": 0
  }
}
```
