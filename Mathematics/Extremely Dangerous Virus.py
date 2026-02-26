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
#  1. INTEGER a
#  2. INTEGER b
#  3. LONG_INTEGER t
#


def solve(a, b, t):
    MOD = 10**9 + 7
    inv2 = pow(2, MOD-2, MOD)  #Modular inverse of 2
    base = (a + b) % MOD
    base = (base * inv2) % MOD
    return pow(base, t, MOD)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    t = int(first_multiple_input[2])

    result = solve(a, b, t)

    fptr.write(str(result) + '\n')

    fptr.close()
