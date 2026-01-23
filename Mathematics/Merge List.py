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
    MOD = 10**9 + 7
    fact = [1] * (n + m + 1) #Precompute factorials up to n + m
    for i in range(1, n + m + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_n = pow(fact[n], MOD - 2, MOD) #Modular inverse via Fermat's Little Theorem
    inv_m = pow(fact[m], MOD - 2, MOD)
    result = fact[n + m] * inv_n % MOD * inv_m % MOD #nCr
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
