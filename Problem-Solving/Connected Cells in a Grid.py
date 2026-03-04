#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False] * m for _ in range(n)]
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True
        size = 0
        while stack:
            x, y = stack.pop()
            size += 1
            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                if (0 <= nx < n and
                    0 <= ny < m and
                    not visited[nx][ny] and
                    matrix[nx][ny] == 1):
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        return size
    max_region = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                region_size = dfs(i, j)
                max_region = max(max_region, region_size)
    return max_region
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
