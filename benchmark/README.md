# Benchmark tests for jenkins-test

This directory contains all the benchmark tests.

## Python Dependencies
* matplotlib
* numpy

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
Time taken - 1 of 5 loops: 0.393783807755
Time taken - 2 of 5 loops: 0.49577498436
Time taken - 3 of 5 loops: 0.510788917542
Time taken - 4 of 5 loops: 0.531482934952
Time taken - 5 of 5 loops: 0.581915140152
Time taken for algo2
Time taken - 1 of 5 loops: 0.122055053711
Time taken - 2 of 5 loops: 0.116642951965
Time taken - 3 of 5 loops: 0.110251903534
Time taken - 4 of 5 loops: 0.119757175446
Time taken - 5 of 5 loops: 0.116226911545
Time taken for algo3
Time taken - 1 of 5 loops: 0.125606060028
Time taken - 2 of 5 loops: 0.119740009308
Time taken - 3 of 5 loops: 0.110261201859
Time taken - 4 of 5 loops: 0.123066186905
Time taken - 5 of 5 loops: 0.1447930336
Time taken for algo4
Time taken - 1 of 5 loops: 0.106407880783
Time taken - 2 of 5 loops: 0.0988380908966
Time taken - 3 of 5 loops: 0.112347841263
Time taken - 4 of 5 loops: 0.105406999588
Time taken - 5 of 5 loops: 0.102222919464

Overall Results
{'algo4': {'average': 0.10504474639892578, 'worst': 0.11234784126281738, 'best': 0.09883809089660645}, 'algo2': {'average': 0.11698679924011231, 'worst': 0.1220550537109375, 'best': 0.11025190353393555}, 'algo3': {'average': 0.12469329833984374, 'worst': 0.14479303359985352, 'best': 0.11026120185852051}, 'algo1': {'average': 0.5027491569519043, 'worst': 0.5819151401519775, 'best': 0.3937838077545166}}
[Finished in 6.0s]
```

The generated graph would be:
![](results.png?raw=true)
