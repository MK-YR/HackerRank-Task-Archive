#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print("yes")
        return
    diff = [i for i in range(n) if arr[i] != sorted_arr[i]]
    if len(diff) == 2:
        print("yes")
        print(f"swap {diff[0]+1} {diff[1]+1}")
    else:
        i, j = diff[0], diff[-1]
        if arr[i:j+1] == list(reversed(sorted_arr[i:j+1])):
            print("yes")
            print(f"reverse {i+1} {j+1}")
        else:
            print("no")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)