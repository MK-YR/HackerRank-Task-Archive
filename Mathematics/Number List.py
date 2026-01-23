#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#

def solve(a, k):
    n = len(a)
    total_subarrays = n * (n + 1) // 2
    count_leq_k = 0
    current_len = 0
    for x in a:
        if x <= k:
            current_len += 1
        else:
            count_leq_k += current_len * (current_len + 1) // 2
            current_len = 0
    count_leq_k += current_len * (current_len + 1) // 2 #Add last segment if it ends with <= k
    return total_subarrays - count_leq_k #Subarrays with maximum > k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = solve(a, k)

        fptr.write(str(result) + '\n')

    fptr.close()
