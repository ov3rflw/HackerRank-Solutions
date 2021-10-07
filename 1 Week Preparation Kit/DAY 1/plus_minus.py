#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here

    greater_ = 0
    less_ = 0
    zero_ = 0
    
    for i in arr:
        if i < 0:
            less_ += 1
        elif i == 0:
            zero_ += 1
        elif i > 0:
            greater_ += 1
            
    print('{0:.6f}'.format(greater_/len(arr)))
    print('{0:.6f}'.format(less_/len(arr)))
    print('{0:.6f}'.format(zero_/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
