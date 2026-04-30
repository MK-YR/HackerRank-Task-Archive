#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(t):
    n = len(t)
    diff = [0] * (n + 1)
    for i in range(n):
        if t[i] >= n:
            continue
        start = (i + 1) % n
        end = (i - t[i] + n) % n
        if start <= end:
            diff[start] += 1
            diff[end + 1] -= 1
        else:
            diff[start] += 1
            diff[n] -= 1
            diff[0] += 1
            diff[end + 1] -= 1
    best = 0
    cur = 0
    ans = 0
    for i in range(n):
        cur += diff[i]
        if cur > best:
            best = cur
            ans = i
    return ans + 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    id = solve(t)

    fptr.write(str(id) + '\n')

    fptr.close()
