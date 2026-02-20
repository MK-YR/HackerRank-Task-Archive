#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y
def solve(a, b, c):
    g, x0, y0 = extended_gcd(a, b)
    x0 *= c // g
    y0 *= c // g
    dx = b // g
    dy = a // g
    denom = a * a + b * b
    t_real = (a * y0 - b * x0) / denom
    candidates = [math.floor(t_real), math.ceil(t_real)]
    best = None
    best_dist = float('inf')
    for t in candidates:
        x = x0 + dx * t
        y = y0 - dy * t
        if x > 0:
            dist = x * x + y * y
            if dist < best_dist or (dist == best_dist and x < best[0]):
                best = (x, y)
                best_dist = dist
    return list(best)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()