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
# The function accepts INTEGER n as parameter.
#

def solve(n):
    MOD = 1000007
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    result = 1
    for p in primes: #For each prime, compute exponent in N!
        exponent = 0
        temp = n
        while temp > 0:
            temp //= p
            exponent += temp
        result = (result * (2 * exponent + 1)) % MOD
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
