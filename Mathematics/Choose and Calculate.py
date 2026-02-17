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
#  1. INTEGER_ARRAY balls
#  2. INTEGER k
#


def solve(balls, k):
    n = len(balls)
    balls.sort()
    MOD = 10 ** 9 + 7
    fact = [1] * (n + 1)  # Precompute factorials and inverse factorials
    inv_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)  # Fermat inverse of factorial[n]
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    ans = 0
    for i in range(n):
        max_count = nCr(i, k - 1)
        min_count = nCr(n - i - 1, k - 1)

        contribution = balls[i] * (max_count - min_count)
        ans = (ans + contribution) % MOD
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    balls = list(map(int, input().rstrip().split()))

    result = solve(balls, k)

    fptr.write(str(result) + '\n')

    fptr.close()
