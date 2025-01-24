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
    zeros = 0
    positives = 0
    negatives = 0
    
    length = len(arr)
    for i in arr:
        if i < 0:
            negatives += 1
        elif i > 0:
            positives += 1
        else:
            zeros += 1
    
    print(positives / length)
    print(negatives / length)
    print(zeros / length)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
