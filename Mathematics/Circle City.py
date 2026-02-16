#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER k
#

def solve(d, k):
    count = 0
    limit = int(math.isqrt(d))
    for x in range(limit + 1):
        y_squared = d - x * x
        y = int(math.isqrt(y_squared))

        if y * y == y_squared:
            if x == 0 and y == 0:
                count += 1
            elif x == 0 or y == 0:
                count += 2
            else:
                count += 4
    if count <= k:
        return "possible"
    else:
        return "impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(d, k)

        fptr.write(result + '\n')

    fptr.close()
