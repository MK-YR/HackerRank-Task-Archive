#!/bin/python3

import math
import os
import sys

def solve(a, queries):
    n = len(a)
    base = a[0]
    diff_gcd = 0
    for i in range(1, n):
        diff = abs(a[i] - base)
        diff_gcd = math.gcd(diff_gcd, diff)
    result = []
    for k in queries:
        if diff_gcd == 0:
            result.append(base + k)
        else:
            result.append(math.gcd(diff_gcd, base + k))
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve(a, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()