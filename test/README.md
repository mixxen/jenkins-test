# Unit test cases for jenkins-test
This directory contains all the unit test cases.

The following test cases are considered for version 0.1.0:

for `models`
* OverflowErrorTest
* ZeroDivisionErrorTest
* FloatingPointErrorTest
* TypeErrorTest
* ValueErrorTest
* RecursionErrorTest
* RuntimeErrorTest

for `run`
* PermissionDeniedTest
* IOErrorTest
* FilePermissionDeniedTest
* FigAvailableTest

####To run as a stand alone file:
```
$ sudo python -m unittest discover <file-name>
```
e.g., `sudo python -m unittest discover test/model_test_overflow.py`

####To run the entire folder:
```
$ sudo python -m unittest discover -s <directory> -p '<regex-pattern>.py'
```
e.g., `sudo python -m unittest discover -s test -p '*_test_*.py'`


### Unit tests for OverFlowError

The following throws an error while executing

Input:

```python
error_funcs.overflow_math_error()
```
Output:
```
F
======================================================================
FAIL: test_overflow (__main__.TestOverflow)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jeril/rdt/algo/jenkins-test/test/test_overflow.py", line 33, in test_overflow
    "The given value doesn't fit the range"
AssertionError: The given value doesn't fit the range

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
[Finished in 0.0s with exit code 1]
```

Input:
```python
error_funcs.overflow_other_error()
```
Output:
```
F
======================================================================
FAIL: test_overflow (__main__.TestOverflow)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jeril/rdt/algo/jenkins-test/test/test_overflow.py", line 33, in test_overflow
    "The given value doesn't fit the range"
AssertionError: The given value doesn't fit the range

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
[Finished in 0.0s with exit code 1]
```

The following does not throw an error while executing

Input:
```python
error_funcs.overflow_no_error()
```
Output:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
[Finished in 0.0s]
```

### Unit tests for ZeroDivisionError

The following throws an error while executing

Input:
```python
error_funcs.zero_division_error()
```
Output:
```
F
======================================================================
FAIL: test_overflow (__main__.TestZeroDivision)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jeril/rdt/algo/jenkins-test/test/test_zerodivision.py", line 33, in test_overflow
    "The denominator cannot be ZERO"
AssertionError: The denominator cannot be ZERO
```

The following does not throw an error while executing

Input:
```python
error_funcs.zero_division_error(5, 2)
```
Output:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
[Finished in 0.0s]
```

The following does not throw an error while executing

Input:
```python
error_funcs.floating_point_error(-4.)
```
Output:
```
F
======================================================================
FAIL: test_overflow (__main__.TestFloatingPoint)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/jeril/rdt/algo/jenkins-test/test/model_test_floatingpoint.py", line 32, in test_overflow
    "The floating point value passed has some problems"
AssertionError: The floating point value passed has some problems

----------------------------------------------------------------------
Ran 1 test in 0.152s

FAILED (failures=1)
```

### Unit tests for FloatingPointError

The following does not throw an error while executing

Input:
```python
error_funcs.floating_point_error(4.)
```
Output:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.222s

OK
[Finished in 0.3s]
```
