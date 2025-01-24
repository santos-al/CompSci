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
    # Write your code here
    largest_num = 0
    smallest_num = arr[0]
    
    smallest_sum = 0
    largest_sum = 0
    
    for i in arr:
        if i > largest_num:
            largest_num = i
        if i < smallest_num:
            smallest_num = i
    
    arr.remove(largest_num)
    for i in arr:
        smallest_sum += i
        
    arr.append(largest_num)
    arr.remove(smallest_num)
    for i in arr:
        largest_sum += i
    
    print(smallest_sum, largest_sum)
        
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
