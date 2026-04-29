#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    n = len(data)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    total_sum = sum(data)
    parent = {1: -1}
    order = []
    stack = [1]
    while stack:
        node = stack.pop()
        order.append(node)
        for nei in graph[node]:
            if nei != parent[node]:
                parent[nei] = node
                stack.append(nei)
    subtree_sum = [0] * (n + 1)

    for node in reversed(order):
        subtree_sum[node] = data[node - 1]
        for nei in graph[node]:
            if nei != parent[node]:
                subtree_sum[node] += subtree_sum[nei]
    min_diff = float('inf')
    for node in range(2, n + 1):
        part = subtree_sum[node]
        diff = abs(total_sum - 2 * part)
        min_diff = min(min_diff, diff)
    return min_diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
