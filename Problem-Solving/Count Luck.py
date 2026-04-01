#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def countLuck(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                start = (i, j)
    visited = [[False]*m for _ in range(n)]
    def dfs(x, y):
        if matrix[x][y] == '*':
            return 0
        visited[x][y] = True
        moves = []
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and matrix[nx][ny] != 'X':
                    moves.append((nx, ny))
        wand = 1 if len(moves) > 1 else 0
        for nx, ny in moves:
            result = dfs(nx, ny)
            if result != -1:
                return result + wand
        return -1
    result = dfs(start[0], start[1])
    return "Impressed" if result == k else "Oops!"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
