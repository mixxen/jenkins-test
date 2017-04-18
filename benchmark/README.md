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
Time taken - 1 of 5 loops: 3.68740606308    Memory used - 1 of 5 loops: 33248488
Time taken - 2 of 5 loops: 1.00408911705    Memory used - 2 of 5 loops: 33250760
Time taken - 3 of 5 loops: 0.942035913467   Memory used - 3 of 5 loops: 33250856
Time taken - 4 of 5 loops: 0.899518966675   Memory used - 4 of 5 loops: 33250856
Time taken - 5 of 5 loops: 1.01477003098    Memory used - 5 of 5 loops: 33250952
Time taken for algo2
Time taken - 1 of 5 loops: 0.541555166245   Memory used - 1 of 5 loops: 33008696
Time taken - 2 of 5 loops: 0.496054172516   Memory used - 2 of 5 loops: 33091336
Time taken - 3 of 5 loops: 0.50258898735    Memory used - 3 of 5 loops: 33091512
Time taken - 4 of 5 loops: 0.504120111465   Memory used - 4 of 5 loops: 33091608
Time taken - 5 of 5 loops: 0.460325956345   Memory used - 5 of 5 loops: 33091608
Time taken for algo3
Time taken - 1 of 5 loops: 0.529996871948   Memory used - 1 of 5 loops: 33009728
Time taken - 2 of 5 loops: 0.501305103302   Memory used - 2 of 5 loops: 33092272
Time taken - 3 of 5 loops: 0.509891033173   Memory used - 3 of 5 loops: 33092544
Time taken - 4 of 5 loops: 0.493989944458   Memory used - 4 of 5 loops: 33092544
Time taken - 5 of 5 loops: 0.483810901642   Memory used - 5 of 5 loops: 33092640
Time taken for algo4
Time taken - 1 of 5 loops: 0.499253988266   Memory used - 1 of 5 loops: 33010664
Time taken - 2 of 5 loops: 0.475882053375   Memory used - 2 of 5 loops: 33093216
Time taken - 3 of 5 loops: 0.449546098709   Memory used - 3 of 5 loops: 33093480
Time taken - 4 of 5 loops: 0.490152835846   Memory used - 4 of 5 loops: 33093576
Time taken - 5 of 5 loops: 0.456408023834   Memory used - 5 of 5 loops: 33093576

Overall Results
{'algo4': {'memory': {'average': 33076902.4, 'worst': 33093576, 'best': 33010664}, 'time': {'average': 0.3906302888250351, 'worst': 0.41563567708492277, 'best': 0.365927787528038}}, 'algo2': {'memory': {'average': 33074952.0, 'worst': 33091608, 'best': 33008696}, 'time': {'average': 0.41731056760311125, 'worst': 0.4579368550634384, 'best': 0.37670764516353605}}, 'algo3': {'memory': {'average': 33075945.6, 'worst': 33092640, 'best': 33009728}, 'time': {'average': 0.42018045972347257, 'worst': 0.44637856076717375, 'best': 0.40019259046077726}}, 'algo1': {'memory': {'average': 33250382.4, 'worst': 33250952, 'best': 33248488}, 'time': {'average': 1.4259457070684434, 'worst': 3.6037877518987655, 'best': 0.8159006554937362}}}
[Finished in 22.7s]
```

The generated graph would be:
![](results.png?raw=true)
