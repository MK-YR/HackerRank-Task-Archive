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
#  1. INTEGER m
#  2. INTEGER a
#

MOD = 10**9 + 7
MAX = 200005
fact = [1] * MAX
invfact = [1] * MAX
for i in range(1, MAX):
    fact[i] = fact[i-1] * i % MOD
invfact[MAX-1] = pow(fact[MAX-1], MOD-2, MOD)
for i in range(MAX-2, -1, -1):
    invfact[i] = invfact[i+1] * (i+1) % MOD
inv2 = pow(2, MOD-2, MOD)
def solve(m, a):
    res = fact[a+m+1] * invfact[a+2] % MOD
    res = res * res % MOD
    res = res * ((a+2) * (a+m+2) % MOD) % MOD
    res = res * pow(inv2, m, MOD) % MOD
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d = int(input().strip())

    for _ in range(d):
        m, a = map(int, input().split())
        result = solve(m, a)
        fptr.write(str(result) + '\n')

    fptr.close()