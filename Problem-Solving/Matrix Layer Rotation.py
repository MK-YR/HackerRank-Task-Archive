#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    layers = min(m, n) // 2
    for layer in range(layers):
        elements = []
        for j in range(layer, n - layer): #Top row
            elements.append(matrix[layer][j])
        for i in range(layer + 1, m - layer - 1): #Right column
            elements.append(matrix[i][n - layer - 1])
        for j in range(n - layer - 1, layer - 1, -1): #Bottom row
            elements.append(matrix[m - layer - 1][j])
        for i in range(m - layer - 2, layer, -1): #Left column
            elements.append(matrix[i][layer])
        rotation = r % len(elements) #Effective rotation
        rotated = elements[rotation:] + elements[:rotation]
        idx = 0
        for j in range(layer, n - layer): #Put back top row
            matrix[layer][j] = rotated[idx]
            idx += 1
        for i in range(layer + 1, m - layer - 1): #Right column
            matrix[i][n - layer - 1] = rotated[idx]
            idx += 1
        for j in range(n - layer - 1, layer - 1, -1): #Bottom row
            matrix[m - layer - 1][j] = rotated[idx]
            idx += 1
        for i in range(m - layer - 2, layer, -1): #Left column
            matrix[i][layer] = rotated[idx]
            idx += 1
    for row in matrix:
        print(*row)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
