# py_package_1

This repository contains a python package that can be installed on any system having python interpreter already installed

clone this repository using
```
git clone https://github.com/vini7148/py_package_1.git
cd py_package_1
```

### Prerequisites

The following tools along with basic knowledge of python and SQL is required to execute this front end

```
python
datetime library (already installed with python interpreter)
```

You can download these needed file using the links below

* [python](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe)

### Installing

To install this python package, execute the following commands in your cli or cmd

```
python test.py
```

![test](https://github.com/vini7148/py_package_1/blob/master/ss/test.png)

This step is to ensure that the package is not broken, if there is no error in the above step procced, else remove the broken package and download it again

```
python setup.py install
```

![setup](https://github.com/vini7148/py_package_1/blob/master/ss/setup.png)

If no errors are shown your are ready to use this package in your system

## Using this package

If you completed the above steps without any errors, you can use this package on your system

to use this package, open a python file and 
```
import test_1
```
or
```
from test_1 import *
```
to imoprt this package in your python file

This package has the following functions

* TIME
```
test_1.time()
```
or
```
time()
```
This function returns the current date and time.
Note: You might want to use this function in a print command to output the time

* Sum
```
test_1.sum(a, b)
```
or
```
sum(a, b)
```
This function returns the sum of a list of numbers that are passed as it's arrguments and are seprated by commas(",").
Note: You might want to use this function in a print command to output the sum

* AVG
```
test_1.avg(a, b)
```
or
```
avg(a, b)
```
This function returns the average of a list of numbers that are passed as it's arrguments and are seprated by commas(",").
Note: You might want to use this function in a print command to output the avg

* HW
```
test_1.hw()
```
or
```
hw()
```
This function returns the f string "Hello World".



## Built with

* [PYTHON](https://www.python.org/)

## Authors

* **Vinayak Goswami** - *Initial work* - [vini7148](https://github.com/vini7148)