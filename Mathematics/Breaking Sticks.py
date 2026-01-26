#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestSequence' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

def longestSequence(a):
    MAXP = 10**6
    is_prime = [True] * (MAXP + 1) #Sieve of Eratosthenes
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAXP**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAXP + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, MAXP + 1) if is_prime[i]]
    def prime_factors_desc(n):
        factors = []
        for p in primes:
            if p * p > n:
                break
            while n % p == 0:
                factors.append(p)
                n //= p
        if n > 1:
            factors.append(n)
        factors.sort(reverse=True)
        return factors
    total_moves = 0
    for L in a:
        factors = prime_factors_desc(L)
        cur = 1
        moves = 1
        for p in factors:
            cur *= p
            moves += cur
        total_moves += moves
    return total_moves

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = longestSequence(a)

    fptr.write(str(result) + '\n')

    fptr.close()