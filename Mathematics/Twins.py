#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def solve(n, m):
    if m < 3:
        return 0
    limit = int(math.isqrt(m)) + 1 #Simple sieve up to sqrt(m)
    base = [True] * (limit + 1)
    base[0] = base[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if base[i]:
            for j in range(i * i, limit + 1, i):
                base[j] = False

    primes = [i for i, is_p in enumerate(base) if is_p]
    size = m - n + 1 #Segmented sieve [n, m]
    segment = [True] * size
    if n == 1:
        segment[0] = False
    for p in primes:
        start = max(p * p, ((n + p - 1) // p) * p)
        for j in range(start, m + 1, p):
            segment[j - n] = False
    count = 0 #Count twin primes
    for i in range(size - 2):
        if segment[i] and segment[i + 2]:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
