#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

from collections import deque

def bfs(n, a, b):
    moves = [
        (a,b),(a,-b),(-a,b),(-a,-b),
        (b,a),(b,-a),(-b,a),(-b,-a)
    ]
    visited = [[False]*n for _ in range(n)]
    q = deque([(0,0,0)])
    visited[0][0] = True
    while q:
        x,y,d = q.popleft()
        if x == n-1 and y == n-1:
            return d
        for dx,dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny,d+1))
    return -1
def knightlOnAChessboard(n):
    result = []
    for a in range(1,n):
        row = []
        for b in range(1,n):
            row.append(bfs(n,a,b))
        result.append(row)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()