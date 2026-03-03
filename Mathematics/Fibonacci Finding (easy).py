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
#  3. INTEGER n
#

#!/bin/python3

MOD = 10**9 + 7
def multiply(a, b):
    return [
        [
            (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
            (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD
        ],
        [
            (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
            (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD
        ]
    ]
# Fast matrix exponentiation
def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]]  #Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        n //= 2
    return result
def solve(A, B, N):
    if N == 0:
        return A % MOD
    if N == 1:
        return B % MOD
    M = [[1, 1], [1, 0]]
    M_power = matrix_power(M, N - 1)
    return (M_power[0][0] * B + M_power[0][1] * A) % MOD
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        n = int(first_multiple_input[2])

        result = solve(a, b, n)

        fptr.write(str(result) + '\n')

    fptr.close()