#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerColoring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def towerColoring(n):
    MOD = 10**9 + 7
    exp = pow(3, n, MOD - 1)
    return pow(3, exp, MOD)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = towerColoring(n)

    fptr.write(str(result) + '\n')

    fptr.close()
