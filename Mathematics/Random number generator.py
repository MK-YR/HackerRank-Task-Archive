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
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def solve(a, b, c):
    A = a
    B = b
    C = c
    total_area = A * B
    m = min(A, B)
    M = max(A, B)
    if C >= A + B:
        return "1/1"
    if C <= m:
        num = C * C
        den = 2 * total_area
    elif C <= M:
        num = 2 * m * C - m * m
        den = 2 * total_area
    else:
        t = A + B - C
        num = 2 * total_area - t * t
        den = 2 * total_area
    g = math.gcd(num, den)
    num //= g
    den //= g
    return f"{num}/{den}"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()