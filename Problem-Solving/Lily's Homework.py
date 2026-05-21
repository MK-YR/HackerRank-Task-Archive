#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def count_swaps(arr, target):
    arr = arr[:]
    index_map = {value: i for i, value in enumerate(arr)}
    swaps = 0
    for i in range(len(arr)):
        correct_value = target[i]
        if arr[i] != correct_value:
            swaps += 1
            swap_index = index_map[correct_value]
            index_map[arr[i]] = swap_index
            index_map[correct_value] = i
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
    return swaps
def lilysHomework(arr):
    ascending = sorted(arr)
    descending = ascending[::-1]
    return min(
        count_swaps(arr, ascending),
        count_swaps(arr, descending)
    )
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
