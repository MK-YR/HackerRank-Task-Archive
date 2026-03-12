#!/bin/python3

import math
import os
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def solve(n, k):
    if (n // 2) * (n - n // 2) <= n * k or n == 1:
        return n - 1
    l, r = 1, n // 2
    while l <= r:
        mid = (l + r) // 2
        if mid * (n - mid) <= n * k:
            l = mid + 1
        else:
            r = mid - 1
    return 2 * r
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())

    for _ in range(q):
        n, k = map(int, input().split())
        result = solve(n, k)
        fptr.write(str(result) + '\n')

    fptr.close()