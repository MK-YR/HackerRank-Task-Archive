#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])
    pluses = []
    for r in range(n):
        for c in range(m):
            if grid[r][c] != 'G':
                continue
            k = 0
            cells = {(r,c)}
            pluses.append((1, set(cells)))
            while True:
                k += 1
                positions = [
                    (r+k, c),
                    (r-k, c),
                    (r, c+k),
                    (r, c-k)
                ]
                if any(
                    x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 'G'
                    for x,y in positions
                ):
                    break
                for p in positions:
                    cells.add(p)
                pluses.append((1 + 4*k, set(cells)))
    max_product = 0
    for i in range(len(pluses)):
        area1, cells1 = pluses[i]
        for j in range(i+1, len(pluses)):
            area2, cells2 = pluses[j]
            if cells1.isdisjoint(cells2):
                max_product = max(max_product, area1 * area2)
    return max_product
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
