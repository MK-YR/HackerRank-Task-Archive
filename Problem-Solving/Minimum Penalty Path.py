#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'beautifulPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY edges
#  2. INTEGER A
#  3. INTEGER B
#

def beautifulPath(edges, A, B):
    n = 0
    for u, v, w in edges:
        n = max(n, u, v)
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    visited = [[False] * 1024 for _ in range(n + 1)]
    q = deque()
    q.append((A, 0))
    visited[A][0] = True
    while q:
        node, penalty = q.popleft()
        for nxt, weight in graph[node]:
            new_penalty = penalty | weight
            if not visited[nxt][new_penalty]:
                visited[nxt][new_penalty] = True
                q.append((nxt, new_penalty))
    for penalty in range(1024):
        if visited[B][penalty]:
            return penalty
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    second_multiple_input = input().rstrip().split()

    A = int(second_multiple_input[0])

    B = int(second_multiple_input[1])

    result = beautifulPath(edges, A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
