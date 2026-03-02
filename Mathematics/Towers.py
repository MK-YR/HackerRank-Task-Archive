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
#  1. LONG_INTEGER n
#  2. INTEGER_ARRAY heights
#

MOD = 10**9 + 7
def matrix_mult(a, b):
    size = len(a)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD
    return result
def matrix_pow(matrix, power):
    size = len(matrix)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        result[i][i] = 1
    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, matrix)
        matrix = matrix_mult(matrix, matrix)
        power //= 2
    return result
def solve(n, heights):
    if n == 0:
        return 2
    max_h = max(heights)
    dp = [0] * (max_h + 1)
    dp[0] = 1
    for i in range(1, max_h + 1):
        for h in heights:
            if i - h >= 0:
                dp[i] = (dp[i] + dp[i - h]) % MOD
    if n <= max_h:
        return (2 * dp[n]) % MOD
    size = max_h
    matrix = [[0] * size for _ in range(size)]
    for h in heights:
        matrix[0][h - 1] = 1
    for i in range(1, size):
        matrix[i][i - 1] = 1
    matrix_n = matrix_pow(matrix, n - max_h)
    state = [dp[max_h - i] for i in range(size)]
    result = 0
    for i in range(size):
        result = (result + matrix_n[0][i] * state[i]) % MOD
    return (2 * result) % MOD
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    heights_count = int(input().strip())

    heights = list(map(int, input().rstrip().split()))

    result = solve(n, heights)

    fptr.write(str(result) + '\n')

    fptr.close()
