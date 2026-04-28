#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    from collections import deque
    n = len(indexes)
    tree = {i + 1: indexes[i] for i in range(n)}
    depth = {}
    queue = deque([(1, 1)])
    while queue:
        node, d = queue.popleft()
        if node == -1:
            continue
        depth[node] = d
        left, right = tree[node]
        if left != -1:
            queue.append((left, d + 1))
        if right != -1:
            queue.append((right, d + 1))
    result = []
    for k in queries:
        for node in tree:
            if depth[node] % k == 0:
                tree[node][0], tree[node][1] = tree[node][1], tree[node][0]
        stack = []
        current = 1
        traversal = []
        while stack or current != -1:
            while current != -1:
                stack.append(current)
                current = tree[current][0]
            current = stack.pop()
            traversal.append(current)
            current = tree[current][1]
        result.append(traversal)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
