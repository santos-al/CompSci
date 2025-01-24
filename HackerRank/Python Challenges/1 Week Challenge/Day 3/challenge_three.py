#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    answer = ""
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                ascii = int(ord(letter)) + k
                if ascii > 90:
                    while (ascii > 90):
                        ascii -= 26
            if letter.islower():
                ascii = int(ord(letter)) + k
                if ascii > 122:
                    while (ascii > 122):
                        ascii -= 26
            answer += chr(ascii)
        else:
            answer += letter
    return answer
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
