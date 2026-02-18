#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix.append(input())
decoded = ''.join(matrix[i][j] for j in range(m) for i in range(n))
decoded = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded)
print(decoded)