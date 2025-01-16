#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_num = arr[0]
    max_num = arr[0]
    total = 0
    
    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        total += num
    
    print(total - max_num, total - min_num)
    
    
    
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
