#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    n = len(arr)
    pos = {value: i for i, value in enumerate(arr)}
    for i in range(n):
        if k == 0:
            break
        correct_value = n - i
        if arr[i] == correct_value:
            continue
        to_swap_idx = pos[correct_value]
        pos[arr[i]] = to_swap_idx
        arr[to_swap_idx] = arr[i]
        arr[i] = correct_value
        pos[correct_value] = i
        k -= 1
    return arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
