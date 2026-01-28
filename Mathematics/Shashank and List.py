#!/bin/python3

import os
import sys

def solve(a):
    MOD = 10**9 + 7
    result = 1
    for x in a:
        result = (result * (1 + pow(2, x, MOD))) % MOD
    return (result - 1) % MOD
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
