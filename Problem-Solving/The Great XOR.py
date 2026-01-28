#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theGreatXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

def theGreatXor(x):
    count = 0
    bit_position = 0
    while x > 0:
        if (x & 1) == 0:
            count += 1 << bit_position
        x >>= 1
        bit_position += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
