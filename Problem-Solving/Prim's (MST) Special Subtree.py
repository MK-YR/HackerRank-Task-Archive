#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    import heapq
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    visited = set()
    min_heap = []
    heapq.heappush(min_heap, (0, start))
    total_weight = 0
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        total_weight += weight
        for next_weight, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (next_weight, neighbor))
    return total_weight
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
