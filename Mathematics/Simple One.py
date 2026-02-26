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
#  1. INTEGER p
#  2. INTEGER q
#  3. INTEGER n
#

def solve(p, q, n):
    MOD = 10**9 + 7
    def complex_mul(a, b):
        return (
            (a[0]*b[0] - a[1]*b[1]) % MOD,
            (a[0]*b[1] + a[1]*b[0]) % MOD
        )
    def complex_pow(base, exp):
        result = (1, 0)
        while exp > 0:
            if exp & 1:
                result = complex_mul(result, base)
            base = complex_mul(base, base)
            exp >>= 1
        return result
    A, B = complex_pow((q % MOD, p % MOD), n)
    invA = pow(A, MOD-2, MOD)
    return (B * invA) % MOD
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = int(first_multiple_input[0])

        q = int(first_multiple_input[1])

        n = int(first_multiple_input[2])

        result = solve(p, q, n)

        fptr.write(str(result) + '\n')

    fptr.close()
