#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    s = list(s)
    changed = [False] * n
    left = 0
    right = n - 1
    while left < right:
        if s[left] != s[right]:
            if k <= 0:
                return "-1"
            if s[left] > s[right]:
                s[right] = s[left]
            else:
                s[left] = s[right]
            changed[left] = changed[right] = True
            k -= 1
        left += 1
        right -= 1
    left = 0
    right = n - 1
    while left <= right and k > 0:
        if left == right:
            if s[left] != '9':
                s[left] = '9'
            break
        if s[left] != '9':
            if changed[left] or changed[right]:
                if k >= 1:
                    s[left] = s[right] = '9'
                    k -= 1
            else:
                if k >= 2:
                    s[left] = s[right] = '9'
                    k -= 2
        left += 1
        right -= 1
    return "".join(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()