#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s[:-2]
    meridiem = s[-2:]
    
    hour, minute, second = time.split(":")
    hour = int(hour)
    
    if meridiem == "AM" and hour == 12:
        hour -= 12
    if meridiem == "PM" and hour != 12:
        hour += 12
    
    form_hour = str(hour).zfill(2)
        
    return f"{form_hour}:{minute}:{second}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
