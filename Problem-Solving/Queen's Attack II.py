#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    #Maximum moves in each direction
    up = n - r_q
    down = r_q - 1
    right = n - c_q
    left = c_q - 1
    up_right = min(up, right)
    up_left = min(up, left)
    down_right = min(down, right)
    down_left = min(down, left)
    for r, c in obstacles:
        if c == c_q:
            if r > r_q:  #Obstacle above
                up = min(up, r - r_q - 1)
            else:  #Obstacle below
                down = min(down, r_q - r - 1)
        elif r == r_q:
            if c > c_q:  #Obstacle right
                right = min(right, c - c_q - 1)
            else:  #Obstacle left
                left = min(left, c_q - c - 1)
        elif abs(r - r_q) == abs(c - c_q):
            if r > r_q and c > c_q:  #Up-right
                up_right = min(up_right, r - r_q - 1)
            elif r > r_q and c < c_q:  #Up-left
                up_left = min(up_left, r - r_q - 1)
            elif r < r_q and c > c_q:  #Down-right
                down_right = min(down_right, r_q - r - 1)
            else:  #Down-left
                down_left = min(down_left, r_q - r - 1)
    return (
        up + down + left + right +
        up_right + up_left + down_right + down_left
    )
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
