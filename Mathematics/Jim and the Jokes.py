#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY dates as parameter.
#

def solve(dates):
    freq = Counter()
    for m, d in dates:
        val = 0
        valid = True
        for ch in str(d):
            digit = int(ch)
            if digit >= m:
                valid = False
                break
            val = val * m + digit
        if valid:
            freq[val] += 1
    jokes = 0
    for count in freq.values():
        jokes += count * (count - 1) // 2
    return jokes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    dates = []

    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    result = solve(dates)

    fptr.write(str(result) + '\n')

    fptr.close()
