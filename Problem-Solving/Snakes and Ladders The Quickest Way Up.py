#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#


def quickestWayUp(ladders, snakes):
    board = {}
    for start, end in ladders:
        board[start] = end
    for start, end in snakes:
        board[start] = end
    visited = [False] * 101
    queue = deque()
    queue.append((1, 0))
    visited[1] = True
    while queue:
        pos, moves = queue.popleft()
        if pos == 100:
            return moves
        for dice in range(1, 7):
            next_pos = pos + dice
            if next_pos > 100:
                continue
            if next_pos in board:
                next_pos = board[next_pos]
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, moves + 1))
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
