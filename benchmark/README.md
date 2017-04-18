# Benchmark tests for jenkins-test

This directory contains all the benchmark tests.

## Python Dependencies
* matplotlib
* numpy
* guppy

The following parameters are to be considered for version 0.1.0:

* Time taken
* Virtual memory or RAM space utilization
* System time
* User time

To run the bechmark tests:
```
$ sudo python benchmark.py
```
This will give the following output:
```
Time taken for algo1
For 1 of 5 loops    Time taken: 0.437947034836  System time: 0.012  User time: 0.424    Memory used: 33265656
For 2 of 5 loops    Time taken: 0.464282989502  System time: 0.008  User time: 0.456    Memory used: 33268104
For 3 of 5 loops    Time taken: 0.437602996826  System time: 0.0    User time: 0.436    Memory used: 33268248
For 4 of 5 loops    Time taken: 0.446910142899  System time: 0.004  User time: 0.444    Memory used: 33268296
For 5 of 5 loops    Time taken: 0.459230184555  System time: 0.004  User time: 0.456    Memory used: 33268440
Time taken for algo2
For 1 of 5 loops    Time taken: 0.145737886429  System time: 0.004  User time: 0.14 Memory used: 33026480
For 2 of 5 loops    Time taken: 0.112924098969  System time: 0.0    User time: 0.112    Memory used: 33109296
For 3 of 5 loops    Time taken: 0.161767959595  System time: 0.0    User time: 0.16 Memory used: 33109608
For 4 of 5 loops    Time taken: 0.116852045059  System time: 0.0    User time: 0.116    Memory used: 33109752
For 5 of 5 loops    Time taken: 0.105036020279  System time: 0.0    User time: 0.104    Memory used: 33109800
Time taken for algo3
For 1 of 5 loops    Time taken: 0.114185810089  System time: 0.0    User time: 0.112    Memory used: 33028216
For 2 of 5 loops    Time taken: 0.116523981094  System time: 0.0    User time: 0.116    Memory used: 33110936
For 3 of 5 loops    Time taken: 0.113718986511  System time: 0.0    User time: 0.112    Memory used: 33111344
For 4 of 5 loops    Time taken: 0.11449098587   System time: 0.0    User time: 0.116    Memory used: 33111392
For 5 of 5 loops    Time taken: 0.104866027832  System time: 0.0    User time: 0.104    Memory used: 33111536
Time taken for algo4
For 1 of 5 loops    Time taken: 0.0981259346008 System time: 0.0    User time: 0.1  Memory used: 33029832
For 2 of 5 loops    Time taken: 0.0889449119568 System time: 0.0    User time: 0.092    Memory used: 33112648
For 3 of 5 loops    Time taken: 0.0960028171539 System time: 0.0    User time: 0.096    Memory used: 33112960
For 4 of 5 loops    Time taken: 0.0967919826508 System time: 0.0    User time: 0.096    Memory used: 33113104
For 5 of 5 loops    Time taken: 0.0913970470428 System time: 0.0    User time: 0.092    Memory used: 33113152

Overall Results
{'algo4': {'sys_time': {'average': 0.0, 'worst': 0.0, 'best': 0.0}, 'memory': {'average': 33096339.2, 'worst': 33113152, 'best': 33029832}, 'user_time': {'average': 0.09519999999999981, 'worst': 0.10000000000000142, 'best': 0.09199999999999875}, 'time': {'average': 0.08589070756292343, 'worst': 0.08976410348272323, 'best': 0.08058308083868027}}, 'algo2': {'sys_time': {'average': 0.0008000000000000007, 'worst': 0.0040000000000000036, 'best': 0.0}, 'memory': {'average': 33092987.2, 'worst': 33109800, 'best': 33026480}, 'user_time': {'average': 0.12640000000000012, 'worst': 0.16000000000000014, 'best': 0.10400000000000098}, 'time': {'average': 0.1201017709479332, 'worst': 0.15340612847661972, 'best': 0.09667418916082382}}, 'algo3': {'sys_time': {'average': 0.0, 'worst': 0.0, 'best': 0.0}, 'memory': {'average': 33094684.8, 'worst': 33111536, 'best': 33028216}, 'user_time': {'average': 0.1120000000000001, 'worst': 0.11600000000000144, 'best': 0.1039999999999992}, 'time': {'average': 0.1043953271613121, 'worst': 0.10816214997625351, 'best': 0.0965041967139244}}, 'algo1': {'sys_time': {'average': 0.005600000000000005, 'worst': 0.01200000000000001, 'best': 0.0}, 'memory': {'average': 33267748.8, 'worst': 33268440, 'best': 33265656}, 'user_time': {'average': 0.4431999999999999, 'worst': 0.4560000000000004, 'best': 0.42399999999999993}, 'time': {'average': 0.44083283860540395, 'worst': 0.4559211583838463, 'best': 0.42924116570806503}}}
[Finished in 19.5s]
```

The generated graph would be:
![](results.png?raw=true)
