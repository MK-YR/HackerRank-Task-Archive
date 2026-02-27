#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts INTEGER_ARRAY P as parameter.
#

def solve(P):
    from math import factorial
    from collections import Counter
    if P == sorted(P):
        return 0.0
    n = len(P)
    freq = Counter(P)
    numerator = factorial(n)
    denominator = 1
    for count in freq.values():
        denominator *= factorial(count)
    return float(numerator / denominator)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    P_count = int(input().strip())

    P = list(map(int, input().rstrip().split()))

    result = solve(P)

    fptr.write(str(result) + '\n')

    fptr.close()
