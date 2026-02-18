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
    a = min(n, m)
    b = max(n, m)
    MOD = 10**9 + 7
    fact = [1] * (a + 1) #Precompute factorials up to a
    for i in range(1, a + 1):
        fact[i] = fact[i - 1] * i % MOD
    result = 1
    for i in range(1, a + 1): #Increasing part: 1!*2!*...*a!
        result = result * fact[i] % MOD
    result = result * pow(fact[a], b - a, MOD) % MOD #Constant middle part: (a!)^(b-a)
    for i in range(1, a): # Decreasing part: (a-1)!*...*1!
        result = result * fact[i] % MOD
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
