# Benchmark tests for jenkins-test

This directory contains all the benchmark tests.

## Python Dependencies
* matplotlib

The following parameters are to be considered for version 0.1.0:

* Time taken
* Virtual memory or RAM space utilization
* CPU utilization
* Total number of CPU-seconds
* Elapsed real (wall clock) time used by the process
* Total number of CPU-seconds used by the system

To run the bechmark tests:
```
$ sudo python benchmark.py
```
This will give the following output:
```
Time taken for algo1
Time taken - 1 of 5 loops: 0.491042852402
Time taken - 2 of 5 loops: 0.550430059433
Time taken - 3 of 5 loops: 0.547604799271
Time taken - 4 of 5 loops: 0.662984848022
Time taken - 5 of 5 loops: 0.574695825577
Time taken for algo2
Time taken - 1 of 5 loops: 0.157751083374
Time taken - 2 of 5 loops: 0.133224964142
Time taken - 3 of 5 loops: 0.131254911423
Time taken - 4 of 5 loops: 0.161274194717
Time taken - 5 of 5 loops: 0.126029014587
Time taken for algo3
Time taken - 1 of 5 loops: 0.123675107956
Time taken - 2 of 5 loops: 0.169538974762
Time taken - 3 of 5 loops: 0.126391172409
Time taken - 4 of 5 loops: 0.172492027283
Time taken - 5 of 5 loops: 0.127220153809
Time taken for algo4
Time taken - 1 of 5 loops: 0.109349012375
Time taken - 2 of 5 loops: 0.106597185135
Time taken - 3 of 5 loops: 0.118223190308
Time taken - 4 of 5 loops: 0.11087012291
Time taken - 5 of 5 loops: 0.142813205719

Overall Results
{'algo4': {'average': 0.11757054328918456, 'worst': 0.14281320571899414, 'best': 0.1065971851348877}, 'algo2': {'average': 0.14190683364868165, 'worst': 0.16127419471740723, 'best': 0.12602901458740234}, 'algo3': {'average': 0.14386348724365233, 'worst': 0.17249202728271484, 'best': 0.12367510795593262}, 'algo1': {'average': 0.5653516769409179, 'worst': 0.6629848480224609, 'best': 0.4910428524017334}}
[Finished in 4.9s]
```
